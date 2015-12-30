from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from datetime import datetime
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render_to_response, RequestContext, redirect

from query.models import Query
from session.models import Session
from django.core.cache import cache


import sys
import os
sys.path.append(os.path.dirname(os.path.realpath('..')))
import uweclang
from . import settings


class QueryForm(forms.Form):
    query = forms.CharField()


class ChangeUsernameForm(forms.Form):
    username1 = forms.CharField()
    username2 = forms.CharField()


class ChangePasswordForm(forms.Form):
    password1 = forms.CharField()
    password2 = forms.CharField()


@login_required(login_url='/#')
def home(request):

    try:
        session_id = request.session['session']
    except:
        return redirect('logout')

    session = Session.objects.get(pk=session_id)
    queries = Query.objects.all().filter(session=session)


    query_form = QueryForm(request.POST or None)

    if request.method == "POST" and 'query' in request.POST and query_form.is_valid():
        query = query_form.cleaned_data['query']
        error_message = ''
        query_results = []
        document = None
        try:
            document = uweclang.QueryDocument(query)
        except uweclang.QueryParseError as e:
            error_message = 'Query parse error {}{}'.format(
                'at line {}, column {}: '.format(e.line, e.column),
                "'{}' ".format(e.text))

        if document:
            try:
                query_results = cache.get('corpus').execute_queries(
                    document.queries,
                    definitions=document.definitions
                )
            except uweclang.QueryExecutionError as e:
                error_message = str(e)

            except uweclang.CorpusError as e:
                error_message = str(e)

            except:
                error_message = "Unknown Error"


            query_results = list(query_results)
            stats = uweclang.compile_statistics(query_results, cache.get('corpus'), ['class', 'semester'])
            if 'semester' in stats:
               semester_stats = stats['semester']
            if 'class' in stats:
               class_stats = stats['class']

            query = Query(user=request.user.username, session=session, date=datetime.now(), query=query, result=stats['total'])
            query.save()




    return render_to_response("home.html", locals(),
                              context_instance=RequestContext(request))


def log_in(request):
    if request.user.is_authenticated(): # Check to see if the user is already logged in
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                # Create new Session
                session = Session(user=username, date=datetime.now())
                session.save()
                # Save Session ID to cookie
                request.session['session'] = session.id

                # Redirect to home
                return redirect('home')
            else:
                messages.error(request, 'Oops!  User is not active')
                return render_to_response("login.html", locals(), context_instance=RequestContext(request))
        else:
            messages.error(request, 'Oops!  User does not exist')
            return render_to_response("login.html", locals(), context_instance=RequestContext(request))

    return render_to_response("login.html", locals(), context_instance=RequestContext(request))


@login_required(login_url='/#')
def log_out(request):
    try:
        logout(request)
    except:
        print ('error logging out')
    return redirect('login')


@login_required(login_url='/#')
def profile(request, session_id):
    try:
        session = Session.objects.get(id__exact=session_id)
    except:
        return redirect('home')

    queries = Query.objects.all().filter(session=session)

    # TODO Change Username
    # TODO Change Password

    username = request.user.username
    username = username.title()
    sessions = Session.objects.all().filter(user=request.user)
    n_logins = len(sessions)

    # TODO display previously ran queries based on category tabs from main results page

    date_joined = request.user.date_joined
    last_login = request.user.last_login
    return render_to_response("profile.html", locals(), context_instance=RequestContext(request))


@login_required(login_url='/#')
def reset_session(request):

    username = request.user.username

    # Create new Session
    session = Session(user=username, date=datetime.now())
    session.save()
    # Save Session ID to cookie
    request.session['session'] = session.id

    # Redirect to home
    return redirect('home')


@login_required(login_url='/#')
def delete_session(request, session_id):
    current_username = request.user.username

    try:
        current_session_id = request.session['session']
        print ('current session id is {}'.format(current_session_id))
    except:
        return redirect('logout')

    try:
        session = Session.objects.get(id__exact=session_id)
        session_username = session.user
        if current_username != session_username:  # attempting to delete session that doesn't belong to you
            return redirect('logout')
    except:
        messages.error(request, 'Error, Session does not exist')
        redirect('profile', session_id=current_session_id)

    if int(session_id) == int(current_session_id):
        print ('session id = current session id')
        messages.error(request, 'Error, Cannot Delete Current Session')
        return redirect('profile', session_id=current_session_id)

    session = Session.objects.get(id__exact=session_id)
    queries = Query.objects.all().filter(session=session)
    for query in queries:
        query.delete()

    session.delete()
    return redirect('profile', session_id=current_session_id)


@login_required(login_url='/#')
def delete_query(request, query_id):
    query = Query.objects.get(id__exact=query_id)
    query.delete()
    return redirect('home')


@login_required(login_url='/#')
def delete_query_from_profile(request, query_id):
    query = Query.objects.get(id__exact=query_id)
    session = query.session
    query.delete()
    return redirect('profile', session_id=session.id)


@login_required(login_url='/#')
def modify(request):
    username = request.user.username
    user = User.objects.get(username=username)

    username_form = ChangeUsernameForm(request.POST or None)
    password_form = ChangePasswordForm(request.POST or None)

    if request.method == "POST" and 'username' in request.POST and username_form.is_valid():
        username1 = username_form.cleaned_data['username1']
        username2 = username_form.cleaned_data['username2']
        if username1 and username1 != username2:
            messages.error(request, 'Error, Usernames did not match')
            return redirect('modify')


        user.username = username1
        user.save()
        messages.success(request, 'Username successfully changed')
        return redirect('logout')

    elif request.method == "POST" and 'password' in request.POST and password_form.is_valid():
        password1 = password_form.cleaned_data['password1']
        password2 = password_form.cleaned_data['password2']


        if password1 and password1 != password2:
            messages.error(request, 'Error, Passwords did not match')
            return redirect('modify')


        queries = Query.objects.all()
        for query in queries:
            query.user = request.user
            query.save()
        sessions = Session.objects.all()
        for session in sessions:
            session.user = request.user
            session.save()

        user.set_password(password1)
        user.save()
        messages.success(request, 'Password successfully changed')
        return redirect('logout')

    return render_to_response("modify.html", locals(), context_instance=RequestContext(request))

from django.contrib import admin
from .models import Session


class SessionAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'user', 'date']
    list_filter = ['user', 'date']
    class Meta:
        model = Session

admin.site.register(Session, SessionAdmin)

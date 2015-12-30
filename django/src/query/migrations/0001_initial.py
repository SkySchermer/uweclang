# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('query', models.CharField(max_length=500)),
                ('result', models.IntegerField()),
                ('session', models.ForeignKey(to='session.Session')),
            ],
        ),
    ]

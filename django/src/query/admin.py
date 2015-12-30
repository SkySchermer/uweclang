from django.contrib import admin
from .models import Query


class QueryAdmin(admin.ModelAdmin):
    list_display = ['query', 'user', 'session', 'date', 'result']
    list_filter = ['user', 'date', 'session']
    class Meta:
        model = Query

admin.site.register(Query, QueryAdmin)

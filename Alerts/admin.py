from django.contrib import admin
from .models import AlertsRules, SeeAlert, SeenBy, Alerts

admin.site.register(AlertsRules)
admin.site.register(SeeAlert)
admin.site.register(SeenBy)
admin.site.register(Alerts)

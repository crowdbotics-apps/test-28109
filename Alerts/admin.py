from django.contrib import admin
from .models import AlertsRules, SeeAlert,SeenBy
admin.site.register(AlertsRules)
admin.site.register(SeeAlert)
admin.site.register(SeenBy)

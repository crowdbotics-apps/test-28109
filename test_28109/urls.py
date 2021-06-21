from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('calendars/', include('calendars.urls')),
    path('patient/', include('patients.urls')),
    path('groups/', include('permissions.urls')),
    path('statistics/', include('timesheets.urls')),
    path('tasks/', include('tasks.urls')),
    path('automation/', include('automations.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

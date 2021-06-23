from django.urls import path
from rest_framework import generics


class AlertsView(generics.ListAPIView):
    """
    #`ws://domain/alerts/?token=<token>`
    <h1 class="label label-primary">connect</h1>
    - "convential I should name it notifcations"

    <h1 class="label label-primary">onmessage</h1>
    - None

    <h1 class="label label-primary">send</h1>
        ```
            {target:'events', id:1, is_seen:true}
        ```
    - note quereis and filters als work here.
    """

    pass


urlpatterns = [
    # path('', admin.site.urls),
    path('', AlertsView.as_view(), name='alerts view'),
]

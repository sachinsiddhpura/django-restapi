from django.urls import path
from .views import Restapi

app_name = 'rest_api'

urlpatterns = [
    path('api/',Restapi.as_view(),name='restapi' ),
]

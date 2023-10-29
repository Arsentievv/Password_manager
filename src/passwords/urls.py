from django.urls import path
from passwords.views import GetPasswordView, GetServiceList


urlpatterns = [
    path('<slug:slug>', GetPasswordView.as_view(), name='get_password'),
    path('', GetServiceList.as_view(), name='service_list'),
]

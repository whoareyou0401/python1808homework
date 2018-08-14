from django.conf.urls import url
from .views import resMsg, filter1

urlpatterns = [
    url(r'^allmsg$',resMsg),
    url(r'name',filter1)
]
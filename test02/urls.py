from django.conf.urls import url
from.views import Hero_all,Hero_u
urlpatterns = [
    url(r'^hero$',Hero_u),
    url(r'^get$',Hero_all)
]
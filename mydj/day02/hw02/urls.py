from django.conf.urls import url
from .views import my_videos,search_by_vn

urlpatterns={
    url(r"^guichu$",my_videos),
    url(r"^getvideo$",search_by_vn)
}
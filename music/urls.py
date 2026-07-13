from django.urls import path
from .views import *
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "music"

urlpatterns = [
    path('singers', views.singer_list_create),
    path('singers/<int:singer_id>/songs', views.song_read_create),
    path('singers/<int:singer_id>', views.singer_detail_update_delete),
    path('tags/<str:tags_name>', views.find_tag),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
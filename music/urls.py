from django.urls import path
from .views import *
from . import views

app_name = "music"

urlpatterns = [
    path('singers', views.singer_list_create),
    path('singers/<int:singer_id>/songs', views.song_read_create),
    path('singers/<int:singer_id>', views.singer_detail_update_delete),
]
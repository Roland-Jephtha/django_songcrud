from django.urls import path
from .views import *


urlpatterns = [
    path ('all', getSongs),
    path ('songs/<int:pk>', getSong),
    path ('add', addSong),
    path ('update/<int:pk>', updatesong),
    path ('delete/<int:pk>', deleteSong),
]

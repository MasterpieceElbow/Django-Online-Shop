from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('room/<int:category_id>/',
         views.category_chat_room,
         name='category_chat_room')
]
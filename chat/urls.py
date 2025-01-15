from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.chat_home, name='chat_home'),
    path('chat/<int:user_id>/', views.start_chat, name='start_chat'),
]

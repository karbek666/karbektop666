from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="boot"),
    path('login/', views.user_login, name='login'),
    path('register/', views.register,name='register'),


]
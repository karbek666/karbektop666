from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('book/', views.index, name="book"),
    path('register/', views.register, name='register'),
    path('sell/', views.sell, name='sell'),
    path('book_tour/', views.book_tour, name='book_tour'),
    path('profile/', views.profile, name='profile'),
    path('poderka/', views.poderka, name='poderka'),
    path('logout/', views.logout_view, name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
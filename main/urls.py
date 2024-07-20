from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('book/', views.index, name="book"),
    path('register/', views.register, name='register'),
    path('sell/', views.sell, name='sell'),
    path('book_tour/<int:pk>/', views.book_tour, name='book_tour'),
    path('profile/', views.profile, name='profile'),
    path('poderka/', views.poderka, name='poderka'),
    path('logout/', views.logout_view, name='logout'),
    path('poderca/', views.poderca, name='poderca'),
    path('<int:pk>/', views.WeenDetailView.as_view(), name='detail'),
    path('buys/<int:pk>/', views.Buy_views.as_view(), name='buy'),
    path('buy/<int:book_id>/', views.process_payment, name='buy_payment'),
    path('delete_favorite/<int:pk>/', views.delete_favorite, name='delete_favorite'),
    path('my_sell/', views.my_sell, name='my_sell'),
    path('delete_my_sell/<int:pk>/', views.delete_my_sell, name='delete_my_sell'),
    path('My_purchases', views.my_purchases, name='my_purchases'),
    path('purchases_tour,/<int:pk>/', views.purchases_tour, name='purchases_tour,'),
    path('make_payment/<int:pk>/', views.make_payment, name='make_payment'),
    # path('send_message/<int:seller_id>/', views.send_message, name='send_message'),
    path('kaif', views.kaif, name='kaif'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
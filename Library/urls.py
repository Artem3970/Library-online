from django.urls import path
from .views import HomeView, ReserveBook
from . import views

urlpatterns = [
    path('/', HomeView.as_view(), name='home'),
    path('', views.home, name='home'),
    path('read_online/<int:book_id>/', views.read_online, name='read_online'),
    path('reservebook/', ReserveBook.as_view(), name='reservebook'),
    path('read_book/<int:book_id>/', views.read_book, name='read_book'),

]




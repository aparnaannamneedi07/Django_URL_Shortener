from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url, name='home'),
    path('<str:short_code>/', views.redirect_url, name='redirect'),
]

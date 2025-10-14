from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inscription/', views.inscription, name='inscription'),
    path('contact/', views.contact, name='contact'),
]


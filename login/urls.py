from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.get_login, name='login'),
    path('logout/', views.get_logout, name="logout")
]

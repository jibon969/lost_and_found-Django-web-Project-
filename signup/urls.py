from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.get_signup, name='signup'),

]

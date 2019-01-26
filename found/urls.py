from django.urls import path
from . import views

urlpatterns = [

    # Found List
    path('found/', views.found, name='found'),


    # Details view
    path('person/<int:id>', views.found_person_details, name='found_person_details'),
    path('item/<int:id>/', views.found_item_details, name='found_item_details'),


    # Create View
    path('create_found_person/', views.create_found_person, name='create_found_person'),
    path('create_found_item/', views.create_found_item, name='create_found_item'),


    # Update view
    path('person/<int:id>/update/', views.found_person_update, name='found_person_update'),
    path('item/<int:id>/update/', views.found_item_update, name='found_item_update'),


    # Delete view
    path('person/<int:id>/delete', views.found_person_delete, name='found_person_delete'),
    path('item/<int:id>/delete', views.found_item_delete, name='found_item_delete'),

]
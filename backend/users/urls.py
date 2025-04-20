from django.contrib import admin
from django.urls import path
from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path('get-users/',UserListCreateView.as_view(), name = 'get-users'), #this is the url for getting all users and creating users
    path('create-user/',UserListCreateView.as_view(), name = 'create-user'), #this is the url for creating users
    path('get-users/<int:id>/', UserDetailView.as_view(), name = 'get-user'), #this is the url for getting a single user and updating ,deleting a user
    path('update/<int:id>/',UserDetailView.as_view(), name = 'update-user'), #this is the url for updating a user
    path('delete/<int:id>/',UserDetailView.as_view(), name = 'delete-user'), #this is the url for deleting a user
]
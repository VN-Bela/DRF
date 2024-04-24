from django.contrib import admin
from django.urls import path
from .views import StudentProfileView,UserListView,StudentCreateRetriveView,UserProfileView
urlpatterns = [
    path('userlist/',UserListView.as_view(), name='userlist'),
    path('userprofile/<int:pk>/',UserProfileView.as_view(), name='userprofile'),
    path('studentdata/',StudentCreateRetriveView.as_view(), name='studentdata'),
    path('studentprofile/<int:pk>/',StudentProfileView.as_view(), name='studentprofile'),
]

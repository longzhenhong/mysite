# lib/urls.py
from django.urls import path
from . import views

app_name = 'lib'
urlpatterns = [
        path('addBook/',views.addBook,name='addBook'),
        path('',views.index,name='index'),
        path('detail/',views.detail,name='detail'),
        ]

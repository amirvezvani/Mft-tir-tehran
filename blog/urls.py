from django.urls import path,include
from . import views
urlpatterns = [
    path('index/',views.index,name=' index'), 
    path('post/',views.post,name=' post'),     
    path('posts/',views.posts,name=' posts'), 
]
from django.contrib import admin
from django.urls import path
from  .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('gippy/', views.gippy, name="gippy"),
    path('treand/meme/', views.trending_meme, name="trend"),
    path('like/<int:meme_id>/', views.like_meme, name="like_meme"), 
    path("search/", views.search, name="search"),  
    path("about/", views.about, name="about"),  
   
]
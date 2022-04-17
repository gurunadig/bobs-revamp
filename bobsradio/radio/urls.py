from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artist', views.artist, name='artist'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('bobstv', views.bobstv, name='bobstv'),
    path('podcast', views.podcast, name='podcast'),
    path('blog', views.blog, name='blog'),
    path('ArtistDetails/<str:pk>', views.artistdetails, name='artistdetails'),
    path('BlogDetails/<str:pk>', views.blogdetails, name='blogdetails')
]

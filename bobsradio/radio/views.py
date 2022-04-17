from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import Artist, Podcast, Radiolink, Blog, Bobstv, Carousel


def home(request):
    artists = Artist.objects.all()[0:4]
    podcasts = Podcast.objects.all()[0:4]
    radiolinks = Radiolink.objects.all()[0:4]
    tvbobs = Bobstv.objects.all()[0:4]
    blogs = Blog.objects.all()[0:4]
    sliders = Carousel.objects.all()
    context = {'artists':artists, 'radiolinks':radiolinks, 'podcasts':podcasts, 'tvbobs':tvbobs, 'blogs':blogs, 'sliders':sliders}
    return render(request, 'radio/radio.html', context)   


def artist(request):
    artists = Artist.objects.all()
    context = {'artists':artists}
    return render(request, 'radio/artist.html', context)   


def about(request):
    return render(request, 'radio/about.html')   


def contact(request):
    return render(request, 'radio/contact.html')   


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'radio/blog.html', context)   

def blogdetails(request, pk):
    blogdetails = Blog.objects.filter(id=pk)
    context = {'blogdetails':blogdetails}
    return render(request, 'radio/BlogDetails.html', context)   


def bobstv(request):
    tvbobs = Bobstv.objects.all()
    context = {'tvbobs':tvbobs}
    return render(request, 'radio/bobstv.html', context)   

def podcast(request):
    podcasts = Podcast.objects.all()
    context = {'podcasts':podcasts}
    return render(request, 'radio/podcast.html', context)   

def artistdetails(request, pk):
    artistdetails = Artist.objects.filter(id=pk)
    context = {'artistdetails':artistdetails}
    return render(request, 'radio/ArtistDetails.html', context)   
"""ticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include, url
from movie import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", views.MovieListView.as_view(), name="main_page"),
    url(r"^movie/(?P<pk>\d+)/$", views.MovieBriefView.as_view(), name="movie_brief"),
    url(r"^moviedetails/(?P<pk>\d+)/$", views.MovieDetailView.as_view(), name="movie_details"),
    url(r"^genrecreate/$", views.MovieGenreCreate.as_view(), name="genre_create"),
    url(r"^moviecreate/(?P<pk>\d+)/$", views.MovieCreateView.as_view(), name="movie_create"),
    url(r"^movieupdate/(?P<pk>\d+)/$", views.MovieUpdateView.as_view(), name="movie_update"),
    url(r"^moviedelete/(?P<pk>\d+)/$", views.MovieDeleteView.as_view(), name="movie_delete"),
    url(r"^genredelete/(?P<pk>\d+)/$", views.GenreDeleteView.as_view(), name="genre_delete"),
    url(r"^bookticket/(?P<pk>\d+)/$", views.BookCreateView.as_view(), name="book_ticket"),

   
    


       
            ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

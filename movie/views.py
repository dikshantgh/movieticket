
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MovieGenre, Movie, Ticket
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from django.http import HttpResponse 
from movie.forms import GenreForm, BookForm,MovieForm
from django.views.generic.edit import FormView

from django.shortcuts import render
from django.shortcuts import get_object_or_404
class MovieGenreCreate(CreateView):
    
    template_name = "movie/GenreCreate.html"
    form_class = GenreForm
    success_url = reverse_lazy('main_page')

class MovieListView(ListView):

    model = MovieGenre
    template_name = "movie/mainpage.html"
    
    def get_context_data(self, **kwargs):
        context = super(MovieListView, self).get_context_data(**kwargs)
        return context
       

class MovieBriefView(DetailView):
    model= MovieGenre
    template_name = "movie/movie.html"
    
    def get_context_data(self, **kwargs):
        
        context = super(MovieBriefView, self).get_context_data(**kwargs)
        context['queryset'] = Movie.objects.all()
        return context

class MovieDetailView(DetailView):
    model= Movie
    template_name = "movie/moviedetails.html"
    
    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        movie_id=self.kwargs['pk']
        movie_all =Movie.objects.get(id = movie_id)
        movie_all.hit_movie = movie_all.hit_movie +1
        context['page']= movie_all.hit_movie 
        movie_all.save()   
        return context



class MovieCreateView(CreateView):

    form_class = MovieForm
    template_name = "movie/create_movie.html"
    success_url = reverse_lazy('main_page' )

    def get_initial(self):
        initials = super(MovieCreateView, self).get_initial()
        initials['moviegenre'] = self.kwargs['pk']
        return initials
    
    def get_context_data(self, **kwargs):
        context = super(MovieCreateView, self).get_context_data(**kwargs)
        movie_id=self.kwargs['pk']
        movie_all =MovieGenre.objects.get(id = movie_id)
        context['k'] = movie_all.name
        return context
        

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "movie/create_movie.html"
    success_url = reverse_lazy('main_page' )
    

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "movie/deletemovie.html"

    success_url = reverse_lazy('main_page')

class GenreDeleteView(DeleteView):
    model = MovieGenre
    template_name = "movie/deletegenre.html"

    success_url = reverse_lazy('main_page')




class BookCreateView(CreateView):
    template_name = "movie/bookticket.html"
   
    form_class =BookForm
    
    def get_initial(self):
        initials = super(BookCreateView, self).get_initial()
        initials['movie'] = self.kwargs['pk']
        return initials    

    
   # def get_context_data(self, **kwargs):
    #    context = super(BookCreateView, self).get_context_data(**kwargs)
     #   l=self.kwargs['pk']
       # pp =Ticket.objects.get(id = l)

        #total_ticket = pp.tickets
        #context['total_ticket'] = Ticket.objects.all().aggregate(Sum('tickets'))
        

      #  return context

    #success_url = reverse_lazy('main_page' )



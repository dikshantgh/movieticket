from django import forms
from django.forms import ModelForm

from .models import MovieGenre, Movie, Ticket


class GenreForm(forms.ModelForm):

    class Meta:
        model = MovieGenre
        fields = '__all__'

        

class MovieForm(forms.ModelForm):
    
    class Meta:
        model = Movie
        #exclude = ['moviegenre']
        fields= ('name','moviegenre','description','url','ticket_limit')
        

    
          
class BookForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

        

    

    
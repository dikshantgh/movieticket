from django import forms

from .models import MovieGenre, Movie, Ticket


class GenreForm(forms.ModelForm):

    class Meta:
        model = MovieGenre
        fields = '__all__'


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # exclude = ['moviegenre']
        fields = ('name', 'description', 'url', 'ticket_limit')
        widgets = {
            'moviegenre': forms.HiddenInput(),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

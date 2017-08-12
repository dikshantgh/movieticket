from django.contrib import admin
from movie.models import Movie,MovieGenre, Ticket

admin.site.register(Movie)
admin.site.register(MovieGenre)
admin.site.register(Ticket)
# Register your models here.
#admin.site.register()


from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.


class MovieGenre(models.Model):

    name = models.CharField(blank=True, max_length=50)
    image = models.ImageField(upload_to="profile_image", blank=True)

    def __str__(self):

        return self.name


class Movie(models.Model):

    name = models.CharField(blank=True, max_length=20)
    moviegenre = models.ForeignKey(MovieGenre, blank=True)
    description = models.TextField(blank=True)
    url = models.TextField(max_length=100, blank=True)
    hit_movie = models.IntegerField(blank=True, default=0)
    ticket_limit = models.IntegerField(blank=True, default=10)

    def __str__(self):
        return self.name + "-" + str(self.moviegenre)


class Ticket(models.Model):

    def validate_number(value):

        if len(str(value)) != 10:
            raise ValidationError(
                ('%(value)s is not a valid number'),
                params={'value': value},
            )

    user = models.OneToOneField(User, max_length=10)
    address = models.CharField(blank=True, max_length=50)
    contact = models.PositiveIntegerField(validators=[validate_number])
    movie = models.ForeignKey(Movie, blank=True, default=1)
    tickets = models.PositiveIntegerField(blank=True, default=0)
    # def get_absolute_url(self):
    #   return reverse ('movie_details',kwargs={'pk':self.pk})

    def __str__(self):

        return str(self.user) + self.address + str(self.contact)

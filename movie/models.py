
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from PIL import Image
from django.core.urlresolvers import reverse

import django.forms

# Create your models here.
class MovieGenre(models.Model):
    name = models.CharField(blank= True, max_length=50)
    image = models.ImageField(upload_to="profile_image",blank=True )
    



    def __str__(self):
        return  self.name 


class Movie(models.Model):
    
    

    name = models.CharField(blank= True, max_length= 20)
    moviegenre = models.ForeignKey(MovieGenre, blank =True, default= 0)
    description = models.TextField(blank = True)
    url = models.TextField(max_length=100,blank=True)
    hit_movie = models.IntegerField(blank = True, default=0)
    ticket_limit = models.IntegerField(blank = True, default =10)
    


    
    
    def __str__(self):
        return self.name + "-" + str(self.moviegenre) + "-" + self.description +"-"+ str(self.ticket_limit)


class Ticket(models.Model):
    
    user = models.OneToOneField(User, max_length = 10)
    address =models.CharField(blank = True, max_length = 50)
    contact = models.IntegerField(blank = True)
    movie = models.ForeignKey(Movie,blank = True, default = 1)
    tickets = models.IntegerField(blank =True, default = 0)
    def get_absolute_url(self):
        return reverse ('movie_details',kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.user) + self.address + str(self.contact)


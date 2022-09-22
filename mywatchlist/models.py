from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length = 200)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    release_date = models.CharField(max_length = 30)
    review = models.TextField()
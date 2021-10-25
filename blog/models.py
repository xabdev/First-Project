from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Consulta(models.Model):
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    text = models.TextField()
    
    def __str__ (self):
        return self.first_name




    


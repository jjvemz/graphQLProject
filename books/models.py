from django.db import models

class Books(models.Model):
    title = models.CharField('Title', max_length=250)
    desc = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
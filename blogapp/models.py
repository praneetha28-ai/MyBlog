from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    
    author = models.SlugField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title 
    
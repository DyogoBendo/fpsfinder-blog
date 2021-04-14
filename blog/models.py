from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)    
    content = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    slang = models.CharField(max_length=25)
    published = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title


class PostFile(models.Model):        
    file = models.FileField(upload_to="images/", blank=True)      
    name = models.CharField(max_length=50)      
    def __str__(self) -> str:        
        return self.name
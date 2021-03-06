from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)    
    content = models.TextField()    
    last_edited_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    banner_link = models.URLField()
    font_banner = models.CharField(max_length=60)
    slug = models.CharField(max_length=55)
    
    def __str__(self) -> str:
        return self.slug


class PostFile(models.Model):        
    file = CloudinaryField('image')    
    name = models.CharField(max_length=50)      
    def __str__(self) -> str:        
        return self.name
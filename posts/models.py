from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content =models.CharField(max_length=150)
    image = models.ImageField(blank=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_posts', blank=True)
    
    def __str__(self) :
        return f'{self.content} {self.image}'

class Comment(models.Model) :
    # comment user
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # comment post
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
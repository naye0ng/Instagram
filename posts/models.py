from django.db import models

# Create your models here.
class Post(models.Model):
    content =models.CharField(max_length=150)
    
    def __str__(self) :
<<<<<<< HEAD
<<<<<<< HEAD
        return self.content
=======
        return slef.content
>>>>>>> b5436e9d3d9f93fa3c0e5215ab95dfceb90a4dd6
=======
        return slef.content
>>>>>>> b5436e9d3d9f93fa3c0e5215ab95dfceb90a4dd6

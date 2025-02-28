from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     photo= models.ImageField(upload_to='profile_photos/', blank=True)
     address=models.TextField(max_length=255, blank=True)
     phone_number=models.CharField(max_length=255, blank=True)
     description= models.TextField(max_length=500, blank=True)

     def __str__(self):
        return self.user.username
class List(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.TextField(max_length=100)
    created_at= models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.user.name


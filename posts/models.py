from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True,null=True)
    profile_picture=models.ImageField(upload_to='profile_pictures/',null=True,blank=True)
    
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    image=models.ImageField(upload_to='post_images/',null=True,blank=True)
    is_deleted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
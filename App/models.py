from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    bio = models.TextField(max_length=150, verbose_name='Bio', null=True)
    profile_image = models.ImageField(upload_to='Profile-Pics', default='default.jpg', verbose_name='Profile Image')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    
    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name_plural = 'Profiles'

class Post(models.Model):
    image = models.ImageField(upload_to='Post-Pics', default='', verbose_name='Post Image', null=False)
    title = models.CharField(max_length=500, verbose_name='Caption', null=False)
    caption = models.CharField(max_length=2200, verbose_name='Caption', null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = 'Image Posts'

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Image Post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Image Post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
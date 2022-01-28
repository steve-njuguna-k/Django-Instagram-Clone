from distutils.command.upload import upload
import imp
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    caption = models.CharField(max_length=2200, verbose_name='Caption', null=False)
    image = models.ImageField(upload_to='Post Pics/', default='https://www.deleuzegroup.com/wp-content/themes/azoomtheme/images/demo/demo-image-default.jpg?x20736', verbose_name='Post Image', null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Date Published')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = 'Posts'

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    bio = models.TextField(max_length=150, verbose_name='Bio', null=True)
    profile_image = models.ImageField(upload_to='Profile Pics/', default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png', verbose_name='Profile Image')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Date Published')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    
    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name_plural = 'Profile'
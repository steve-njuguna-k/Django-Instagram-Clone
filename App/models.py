from sre_parse import CATEGORIES
from django.db import models
from django.contrib.auth.models import User

COUNTY = [
    ('Baringo', ('Baringo')),
    ('Bomet', ('Bomet')),
    ('Bungoma', ('Bungoma')),
    ('Busia', ('Busia')),
    ('Elgeyo-Marakwet', ('Elgeyo-Marakwet')),
    ('Embu', ('Embu')),
    ('Garissa', ('Garissa')),
    ('Homa Bay', ('Homa Bay')),
    ('Isiolo', ('Isiolo')),
    ('Kajiado', ('Kajiado')),
    ('Kakamega', ('Kakamega')),
    ('Kericho', ('Kericho')),
    ('Kiambu', ('Kiambu')),
    ('Kilifi', ('Kilifi')),
    ('Kirinyaga', ('Kirinyaga')),
    ('Kisii', ('Kisii')),
    ('Kisumu', ('Kisumu')),
    ('Kitui', ('Kitui')),
    ('Kwale', ('Kwale')),
    ('Laikipia', ('Laikipia')),
    ('Lamu', ('Lamu')),
    ('Machakos', ('Machakos')),
    ('Makueni', ('Makueni')),
    ('Mandera', ('Mandera')),
    ('Marsabit', ('Marsabit')),
    ('Meru', ('Meru')),
    ('Migori', ('Migori')),
    ('Mombasa', ('Mombasa')),
    ("Murang'a", ("Murang'a")),
    ('Nairobi', ('Nairobi')),
    ('Nakuru', ('Nakuru')),
    ('Nandi', ('Nandi')),
    ('Narok', ('Narok')),
    ('Nyamira', ('Nyamira')),
    ('Nyandarua', ('Nyandarua')),
    ('Nyeri', ('Nyeri')),
    ('Samburu', ('Samburu')),
    ('Siaya', ('Siaya')),
    ('Taita–Taveta', ('Taita–Taveta')),
    ('Tana River', ('Tana River')),
    ('Tharaka-Nithi', ('Tharaka-Nithi')),
    ('Trans-Nzoia', ('Trans-Nzoia')),
    ('Turkana', ('Turkana')),
    ('Uasin Gishu', ('Uasin Gishu')),
    ('Vihiga', ('Vihiga')),
    ('Wajir', ('Wajir')),
    ('West Pokot', ('West Pokot')),
]

CATEGORIES = [
    ('Business', ('Business')),
    ('Beach', ('Beach')),
    ('Wallpaper', ('Wallpaper')),
    ('Love', ('Love')),
    ('Flower', ('Flower')),
    ('Nature', ('Nature')),
    ('People', ('People')),
    ('Girl', ('Girl')),
    ('Food', ('Food')),
    ('Sad', ('Sad')),
    ('Computer', ('Computer')),
    ('Office', ('Office')),
    ('City', ('City')),
    ('Cars', ('Cars')),
    ('Black And White', ('Black And White')),
    ('Travel', ('Travel')),
    ('Fashion', ('Fashion')),
    ('Music', ('Music')),
    ('House', ('House')),
    ('Work', ('Work')),
    ('Flowers', ('Flowers')),
    ('Health', ('Health')),
    ('Laptop', ('Laptop')),
    ('Art', ('Art')),
    ('Technology', ('Technology')),
    ('Abstract', ('Abstract')),
    ('Sport', ('Sport')),
    ('Space', ('Space')),
    ('Landscape', ('Landscape')),
    ('Architecture', ('Architecture')),
]

# Create your models here.
class Category(models.Model):
    name = models.CharField(choices=CATEGORIES, max_length=50, verbose_name='Category', null=False)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = 'Categories'

class County(models.Model):
    name = models.CharField(choices=COUNTY, max_length=50, verbose_name='name', null=False)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = 'Counties'

class ImagePost(models.Model):
    caption = models.CharField(max_length=2200, verbose_name='Caption', null=False)
    image = models.ImageField(upload_to='Post-Pics', default='', verbose_name='Post Image', null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    county = models.ForeignKey(County, on_delete=models.CASCADE, verbose_name='County')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = 'Image Posts'

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
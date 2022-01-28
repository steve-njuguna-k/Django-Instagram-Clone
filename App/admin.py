from django.contrib import admin
from .models import Posts, Profile

# Register your models here.
admin.site.register(Posts) 
admin.site.register(Profile)
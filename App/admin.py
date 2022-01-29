from django.contrib import admin
from .models import ImagePost, Profile, County, Category

# Register your models here.
admin.site.register(ImagePost) 
admin.site.register(County) 
admin.site.register(Category) 

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_image', 'bio', 'date_created', 'date_updated')
    search_fields = []
    readonly_fields=('date_created', 'date_updated')
    
admin.site.register(Profile, ProfileAdmin)
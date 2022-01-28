from django.contrib import admin
from .models import Posts, Profile

# Register your models here.
admin.site.register(Posts) 
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_image', 'bio', 'date_published', 'date_updated')
    search_fields = []
    readonly_fields=('date_published', 'date_updated')
    
admin.site.register(Profile, ProfileAdmin)
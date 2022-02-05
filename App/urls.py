from django.urls import path
from App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name="Home"),
    path('login', views.Login, name="Login"),
    path('register', views.Register, name="Register"),
    path('profile', views.Profile, name="Profile"),
    path('profile/<str:username>/edit', views.EditProfile, name="EditProfile"),
    path('profile/<str:username>/settings', views.Settings, name="Settings"),
    path('post/add', views.AddPost, name="AddPost"),
    path('logout', views.Logout, name="Logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
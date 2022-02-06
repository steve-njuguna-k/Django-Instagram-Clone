from django.urls import path
from App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name="Home"),
    path('login', views.Login, name="Login"),
    path('register', views.Register, name="Register"),
    path('profile/<str:username>', views.Profile, name="Profile"),
    path('profile/<str:username>/edit', views.EditProfile, name="EditProfile"),
    path('profile/<str:username>/settings', views.Settings, name="Settings"),
    path('post/<str:title>', views.SingleImage, name="SingleImage"),
    path('profile/<str:username>/image/add', views.AddNewPost, name="AddNewPost"),
    path('logout', views.Logout, name="Logout"),
    path('search-results', views.Search, name="Search"),
    path('activateuser/<uidb64>/<token>', views.ActivateAccount, name = 'ActivateAccount')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
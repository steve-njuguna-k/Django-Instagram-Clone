from django.urls import path
from App import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('login', views.Login, name="Login"),
    path('register', views.Register, name="Register"),
    path('profile', views.Profile, name="Profile"),
    path('profile/<str:username>/edit', views.EditProfile, name="EditProfile"),
    path('logout', views.Logout, name="Logout")
]

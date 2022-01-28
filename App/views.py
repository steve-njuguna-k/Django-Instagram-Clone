from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request, 'Login.html')

def Register(request):
    return render(request, 'Register.html')

def Home(request):
    return render(request, 'Index.html')

def Profile(request):
    return render(request, 'Profile.html')
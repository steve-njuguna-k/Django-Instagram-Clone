from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def Login(request):
    return render(request, 'Login.html')

def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error('⚠️ Passwords Do Not Match! Try Again')
            return redirect('Register')

        if User.objects.filter(username=username).exists():
            messages.error('⚠️ Username Already Exists! Choose Another One')
            return redirect('Register')

        if User.objects.filter(email=email).exists():
            messages.error('⚠️ Email Address Already Exists! Choose Another One')
            return redirect('Register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password1)
        user.save()

        messages.success(request, '✅ Regristration Successful! You can now log in.')
        return redirect('Register')

    return render(request, 'Register.html')

@login_required(login_url='Login')
def Home(request):
    return render(request, 'Index.html')

@login_required(login_url='Login')
def Profile(request):
    return render(request, 'Profile.html')

@login_required(login_url='Login')
def Logout(request):
    return render(request, 'Login.html')
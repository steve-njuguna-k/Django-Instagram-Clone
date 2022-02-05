from ast import Add
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import UpdateUserForm, UpdateProfileForm, AddPostForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, '⚠️ Passwords Do Not Match! Try Again')
            return redirect('Register')

        if User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Username Already Exists! Choose Another One')
            return redirect('Register')

        if User.objects.filter(email=email).exists():
            messages.error(request, '⚠️ Email Address Already Exists! Choose Another One')
            return redirect('Register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password1)
        user.save()

        messages.success(request, '✅ Regristration Successful! You can now log in.')
        return redirect('Register')

    return render(request, 'Register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if not User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Username Does Not Exist! Choose Another One')
            return redirect('Login')

        if user is None:
            messages.error(request, '⚠️ Username or Password Is Incorrect!! Please Try Again')
            return redirect('Login')

        if user is not None:
            login(request, user)
            return redirect(reverse('Home'))
        
    return render(request, 'Login.html')

@login_required(login_url='Login')
def Logout(request):
    logout(request)
    messages.success(request, '✅ Successfully Logged Out!')
    return redirect(reverse('Login'))


@login_required(login_url='Login')
def Home(request):

    return render(request, 'Index.html')

@login_required(login_url='Login')
def Profile(request):
    return render(request, 'Profile.html')

@login_required(login_url='Login')
def EditProfile(request, username):
    user = User.objects.filter(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, '✅ Your Profile Has Been Updated Successfully!')
            return redirect('Profile')
        else:
            messages.error(request, "⚠️ Your Profile Wasn't Updated!")
            return redirect('EditProfile', username=username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'Edit Profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required(login_url='Login')
def Settings(request, username):
    username = User.objects.filter(username=username)
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, '✅ Your Password Has Been Updated Successfully!')
            return redirect("Profile")
        else:
            messages.error(request, "⚠️ Your Password Wasn't Updated!")
            return redirect("Settings", username=username)
    else:
        form = PasswordChangeForm(data=request.POST, user=request.user)
        return render(request, "Settings.html", {'form': form})

@login_required(login_url='Login')
def AddPost(request):
    form = AddPostForm()
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Your Post Was Created Successfully!')
            return redirect('Profile')
        else:
            messages.error(request, "⚠️ Your Post Wasn't Created!")
            return redirect('AddPost')
    else:
        form = AddPostForm(request.POST, request.FILES, instance=request.user)

    return render(request, 'Add Post.html', {'form': form})
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import UpdateUserForm, UpdateProfileForm, AddPostForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .models import Like, Post, Profile, Comment

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
        user.is_active = False
        user.save()

        current_site = get_current_site(request)
        subject = 'Activate Your InstaPics Account'
        message = render_to_string('Account Activation Email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
        })
        user.email_user(subject, message)

        messages.success(request, '✅ Regristration Successful! An Activation Link Has Been Sent To Your Email')
        return redirect('Register')

    return render(request, 'Register.html')

def ActivateAccount(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        messages.success(request, ('✅ Email Verified! You can now Log in'))
        return redirect('Login')
    else:
        messages.error(request, ('⚠️ The confirmation link was invalid, possibly because it has already been used.'))
        return redirect('Login')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # if user and not user.profile.email_confirmed:
        #     messages.error(request, '⚠️ Email is not verified, please check your inbox')
        #     return render(request, 'Login.html')

        if not User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Username Does Not Exist! Choose Another One')
            return redirect('Login')

        if user is None:
            messages.error(request, '⚠️ Username/Password Is Incorrect or Account Is Not Activated!! Please Try Again')
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
    posts = Post.objects.order_by('-date_created').all()
    return render(request, 'Index.html', {'posts':posts})

@login_required(login_url='Login')
def UserProfile(request, username):
    profile = User.objects.get(username=username)
    profile_details = Profile.objects.get(user = profile.id)
    images = Post.objects.filter(author = profile.id).all()
    images_count = Post.objects.filter(author = profile.id)
    return render(request, 'User Profile.html', {'profile':profile, 'profile_details':profile_details, 'images':images, 'images_count':images_count})

@login_required(login_url='Login')
def MyProfile(request, username):
    profile = User.objects.get(username=username)
    profile_details = Profile.objects.get(user = profile.id)
    images = Post.objects.filter(author = profile.id).all()
    images_count = Post.objects.filter(author = profile.id)
    return render(request, 'My Profile.html', {'profile':profile, 'profile_details':profile_details, 'images':images, 'images_count':images_count})

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
            return redirect('MyProfile', username=username)
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
            return redirect("MyProfile", username=username)
        else:
            messages.error(request, "⚠️ Your Password Wasn't Updated!")
            return redirect("Settings", username=username)
    else:
        form = PasswordChangeForm(data=request.POST, user=request.user)
        return render(request, "Settings.html", {'form': form})

def SingleImage(request, id):
    post = Post.objects.get(id = id)
    print(post)
    likes = Like.objects.filter(post = post.id).count()
    print(likes)
    comments = Comment.objects.filter(post = post.id).count()
    print(comments)
    return render(request, 'Post Details.html', {'post': post, 'comments':comments, 'likes':likes})

@login_required(login_url='Login')
def AddNewPost(request, username):
    form = AddPostForm()
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.profile = request.user.profile
            post.save()
            messages.success(request, '✅ Your Post Was Created Successfully!')
            return redirect('MyProfile', username=username)
        else:
            messages.error(request, "⚠️ Your Post Wasn't Created!")
            return redirect('AddNewPost', username=username)
    else:
        form = AddPostForm()
    return render(request, 'Add Post.html', {'form':form})

def Search(request):
    if request.method == 'POST':
        search = request.POST['imageSearch']
        users = User.objects.filter(username__icontains = search).all()
        if not users:
            return render(request, 'Search Results.html', {'search':search, 'users':users})
        else:
            images = Post.objects.filter(author = users[0]).all()
            images_count = Post.objects.filter(author = users[0])
            return render(request, 'Search Results.html', {'search':search, 'users':users, 'images':images, 'images_count':images_count})
    else:
        return render(request, 'Search Results.html')

@login_required(login_url='Login')
def AddComment(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        usercomment = request.POST['comment']
        comment_obj = Comment.objects.create(opinion = usercomment, author = request.user, post = post)
        comment_obj.save()
        messages.success(request, '✅ Your Comment Was Created Successfully!')
        return redirect('Home')
    else:
        messages.error(request, "⚠️ Your Comment Wasn't Created!")
        return redirect('Home')

@login_required(login_url='Login')
def PostLike(request,id):
    postTobeliked = Post.objects.get(id = id)
    currentUser = User.objects.get(id = request.user.id)
    if not postTobeliked:
        return "Post Not Found!"
    else:
        like = Like.objects.filter(author = currentUser, post = postTobeliked)
        if like:
            messages.error(request, '⚠️ You Can Only Like A Post Once!')
            return redirect('Home')
        else:
            likeToadd = Like(author = currentUser, post = postTobeliked)
            likeToadd.save()
            messages.success(request, '✅ You Successfully Liked The Post!')
            return redirect('Home')
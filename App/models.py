from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    bio = models.TextField(max_length=150, verbose_name='Bio', null=True)
    profile_image = CloudinaryField('profile_image')
    email_confirmed = models.BooleanField(default=False, verbose_name='Is Confirmed?')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def get_posts(self):
        return Post.objects.filter(user=self).all()

    def get_followers(self): # people who follow the user
        return self.followers.all()

    def get_following(self): # people who the user follow
        return self.following.all()
    
    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name_plural = 'Profiles'

class Post(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=500, verbose_name='Caption', null=False)
    caption = models.CharField(max_length=2200, verbose_name='Caption', null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Profile')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def get_posts(self):
        return Post.objects.filter(user=self).all()
    
    def get_likes(self):
        likes = Like.objects.filter(post=self)
        return len(likes)

    def get_comments(self):
        comments = Comment.objects.filter(post=self)
        return comments

    @classmethod
    def update_caption(cls, id, title, caption, author, profile):
        update = cls.objects.filter(id = id).update(title = title , caption = caption, author = author, profile = profile)
        return update
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Follow(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

class Comment(models.Model):
    opinion = models.CharField(max_length=2200, verbose_name='Comment', null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def display_comment(self,post_id):
        comments = Comment.objects.filter(self = post_id)
        return comments

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = 'Comments'
from .models import Comment, Post, Follow, Like, Profile
from django.test import TestCase
from django.contrib.auth.models import User

user = User.objects.get(id=1)

class TestFollowers(TestCase):
    def setUp(self):
        self.new_user=User(first_name='John', last_name='Doe', username='user', email='user@gmail.com',password='user')
        self.new_user.save()
        user=Follow(user='user',following=1)
        user.save()

    def test_instance(self):
        self.assertTrue(isinstance(user, Follow))

class TestLike(TestCase):
    def setUp(self):
        self.new_user=User(first_name='John', last_name='Doe', username='user', email='user@gmail.com',password='user')
        self.new_user.save()
        user=Like(author=1, post=1)
        user.save()

    def test_instance(self):
        self.assertTrue(isinstance(user,Like))
    
class TestComment(TestCase):
    def setUp(self):
        self.new_comment=Comment(comment='comment', author=user, post=self.new_post)
        self.new_comment.save()

class TestPost(TestCase):
    def setUp(self):
        self.new_post=Post(image = "default.jpg", title="Title", caption='hello world', author=user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_save_image(self):
        new_p=self.new_post
        new_p.save_image()
        posts=Post.get_posts()
        self.assertTrue(len(posts)>0)

    def update_image(self):
        new_p=self.new_post
        new_p.update_caption()
        posts=Post.get_posts()
        self.assertTrue(len(posts)==0)

    def test_delete_image(self):
        new_p=self.new_post
        new_p.delete_image()
        posts=Post.get_posts()
        self.assertTrue(len(posts)==0)

class TestUserProfile(TestCase):
    def setUp(self):
        self.new_user=User(first_name='John', last_name='Doe', username='user', email='user@gmail.com',password='user')
        self.new_user.save()

        self.profile=Profile(user=user, bio='this is me', profile_image='profile.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
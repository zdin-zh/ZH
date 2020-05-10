from django.db import models
from django.forms import ModelForm

# Create your models here.
class BaseProfile(models.Model):
    username = models.CharField("Username", max_length=10, unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username
    class Meta:
        abstract = True
class Post(models.Model):

    name = models.CharField(max_length=100)
    imageFile = models.ImageField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("upload", kwargs={'username':self.user.username,"id": self.id})

    class Meta:
        ordering = ["-updated"]         

class Profile(BaseProfile):
    pass

class Account(BaseProfile):
    logged = models.BooleanField(default=False)

class SignupForm(ModelForm):
    class Meta:
        model=Profile
        fields = ['username','password']

class Upload(models.Model):
    name = models.CharField(max_length=30)
  
    image = models.URLField()

class Friends(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE,)#updated on 02-12-2018 added on_delete
    friend_id = models.CharField(max_length=10)
    friend_added = models.BooleanField(default=False)
    def __str__(self):
        return self.friend_id #changes admin Users>fname

class Messages(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE,)#updated on 02-12-2018 added on_delete
    friend = models.ForeignKey('Friends', on_delete=models.CASCADE,)#updated on 02-12-2018 added on_delete
    message = models.TextField(max_length=500)
    #created_date = models.DateTimeField(editable=False, default=timezone.now())

class SavedMessages(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, )
    friend = models.ForeignKey('Friends', on_delete=models.CASCADE,)
    message = models.TextField(max_length=500)

class Notifications(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, )
    friend_id = models.CharField(max_length=10)
    message = models.TextField(max_length=280)
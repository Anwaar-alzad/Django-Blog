from django.db import models
from django.conf import settings
# from django.contrib.auth.models import AbstractUser


# # customizable user
# class User(AbstractUser):
#     pass

class Member(models.Model):
    firstname = models.CharField(max_length = 250)
    lastname = models.CharField(max_length = 250)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    address = models.CharField(max_length = 150, null=True)
    
    
    
    class Meta:
        verbose_name = ("Member")
        verbose_name_plural = ("Members")
        app_label = 'feedapp'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Member_detail", kwargs={"pk": self.pk})


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length = 150)
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=False)
    hidden = models.BooleanField()
    date_hidden = models.DateTimeField(auto_now=False, auto_now_add=False)
    # used only when a moderator decides to hide a post
    hidden_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='mod_who_hid')


        
    
    

    

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})

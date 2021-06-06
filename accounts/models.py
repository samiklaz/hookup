from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Custom', 'Custom')
)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    gender = models.CharField(choices=GENDER_CHOICES, default='Custom', max_length=30)
    phone_number = models.CharField(max_length=20)
    birthday = models.IntegerField(default=0)
    ip_address = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)

    def create_account(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(user=instance)
            Profile.objects.create(user=instance)

    post_save.connect(create_account, sender=User)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_image = models.FileField(upload_to="profiles", default="profiles/default/default.png")
    bio = models.CharField(max_length=100, blank=True)
    connection = models.CharField(max_length=50, blank=True)
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)


class Data(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.IntegerField(default=0)

    def __str__(self):
        return self.username

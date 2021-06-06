from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.FileField(upload_to="posts", blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' - ' + str(self.text)

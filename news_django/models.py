from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    birthday = models.DateField(blank=True)
    email = models.CharField(max_length=180, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class New(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    flag = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class NewComment(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text} (from: {self.user.email})"
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='user-profile', default='default.png', blank=True, null=True)
    ssn = models.CharField(max_length=9, null=True)
    number = models.CharField(max_length=13, null=True)
    nation_id = models.CharField(max_length=11, null=True)
    specialization = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=3, null=True)
    job_saved = []

    def __str__(self):
        return self.user.username


class JobPost(models.Model):
    job_role = models.CharField(max_length=100)
    company_logo = models.FileField(upload_to='logos', blank=True, null=True)
    address = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    company = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.job_role
    

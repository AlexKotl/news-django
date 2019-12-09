from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import MyUser, New, NewComment

admin.site.register(MyUser)
admin.site.register(New)
admin.site.register(NewComment)
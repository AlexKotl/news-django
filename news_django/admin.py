from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

admin.site.register(MyUser)
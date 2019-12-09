from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View, generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages

class IndexView(View):
    def get(self, request):
        return render(request, 'homepage.html')

class RegisterView(generic.CreateView):
    pass
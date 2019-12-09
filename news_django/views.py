from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View, generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import MyUserCreationForm, NewCreationForm
from .models import MyUser

class IndexView(View):
    def get(self, request):
        return render(request, 'homepage.html')

class AddView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = NewCreationForm
    success_url = reverse_lazy('index')
    success_message = "Your new was added. "
    template_name = 'add.html'

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = MyUser.objects.get(pk=self.request.user.id)
        self.object.save()
        messages.success(self.request, self.success_message) # force add message, mixin will not work in overrided method
        return HttpResponseRedirect(self.get_success_url())

class RegisterView(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'
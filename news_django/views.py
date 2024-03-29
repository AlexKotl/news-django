import requests
import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View, generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings
from .forms import MyUserCreationForm, NewCreationForm, NewCommentCreationForm
from .models import MyUser, New, NewComment
from .tasks import mail

class IndexView(View):
    def get(self, request):
        return render(request, 'homepage.html', {
            "news": New.objects.filter().order_by("-pk")
        })

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

class DetailsView(View):
    def get(self, request, id):
        new = New.objects.get(pk=id)
        return render(request, 'details.html', {
            "new": new,
            "comments": NewComment.objects.filter(new=new),
            "comment_form": NewCommentCreationForm,
        })

    def post(self, request, id):
        new = New.objects.get(pk=id)

        try:
            comment = NewComment(
                text=request.POST.get('text'),
                new=new,
                user=MyUser.objects.get(pk=request.user.id))
            comment.save()
        except:
            messages.error(self.request, "Failed to add comment. Contact administrator.")
            return HttpResponseRedirect("{}".format(reverse('details', args=(id,))))


        mail.delay(new.user.email, "New comment", "You received new comment!")

        messages.success(self.request, "Comment added")
        return HttpResponseRedirect("{}".format(reverse('details', args=(id,))))

class RegisterView(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'

    def form_valid(self, form):
        r = requests.get(
            "https://api.mailgun.net/v4/address/validate",
            auth=("api", os.environ["MAILGUN_API_KEY"]),
            params={"address": self.request.POST.get("email")})
        is_valid_email = r.json()["result"] == "deliverable"
        if not is_valid_email:
            raise ValidationError("Invalid email", code="invalid_email")

        return super().form_valid(form)

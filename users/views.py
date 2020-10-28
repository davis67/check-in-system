from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views import View
from . import forms, models


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            loggedInUser = models.User.objects.get(email=email)
            user = authenticate(
                request=request, username=loggedInUser.username, password=password
            )
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))

        return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("users:login"))


class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = forms.RegisterForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        return super().form_invalid(form)

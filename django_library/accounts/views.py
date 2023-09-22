from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from accounts.forms import UserRegistrationForm
from django.http.response import HttpResponseBadRequest
from django.views.decorators.debug import sensitive_variables, sensitive_post_parameters


class RegistrationView(TemplateView):
    template_name = 'registration/registration.html'

    def get(self, request):
        context = {
            'form': UserRegistrationForm(request.POST)
        }
        return render(request, self.template_name, context)

    # @method_decorator(sensitive_post_parameters())
    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if not form.data["email"]:
            return HttpResponseBadRequest

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

from django.shortcuts import render
from django.views import View
from .forms import RegistrationForm


class Register(View):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        pass



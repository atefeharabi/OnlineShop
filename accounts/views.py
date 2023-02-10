from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
import random
from core.utils import send_otp_code
from core.models import OptCode


class Register(View):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(10000, 99999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OptCode.objects.create(phone=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'We sent you a code', 'success')
            return redirect('accounts:verify_code')
        return redirect('products:home')


class VerifyCode(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

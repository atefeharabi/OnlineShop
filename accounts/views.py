from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm, VerifyCodeForm, UserLoginForm
from .models import User
import random
from core.utils import send_otp_code
from core.models import OtpCode
from django.contrib.auth import authenticate, login, logout


class Register(View):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            # the print statements is just for having the generated code without sign in as admin
            # and reading from admin panel, it must remove after buy sms sending service and set api
            print(random_code)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'We sent you a code', 'success')
            return redirect('accounts:verify_code')

        return render(request, self.template_name, {'form': form})


class VerifyCode(View):
    form_class = VerifyCodeForm
    template_name = 'accounts/verify.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone=user_session['phone'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                if code_instance.is_expired():
                    messages.error(request, 'code was expired.', 'danger')
                    return redirect('accounts:register')
                else:
                    User.objects.create_user(user_session['email'], user_session['phone'], user_session['password'])
                    code_instance.delete()
                    messages.success(request, 'Registration done successfully', 'success')
                    return redirect('products:home')
            else:
                messages.error(request, 'Verification code is incorrect', 'danger')
                return redirect('accounts:verify_code')

        return redirect('products:home')


class Login(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully', 'success')
                if request.session['cart']:
                    return redirect('orders:cart')
                return redirect('products:home')
            else:
                messages.error(request, 'Username or Password is wrong', 'danger')
                return render(request, self.template_name, {'form': form})


class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'logged out successfully', 'success')
        return redirect('products:home')

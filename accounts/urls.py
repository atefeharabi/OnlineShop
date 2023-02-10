from django.urls import path
from .views import Register, VerifyCode

app_name = 'accounts'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('verify/', VerifyCode.as_view(), name='verify_code')
]
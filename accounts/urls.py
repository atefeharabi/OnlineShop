from django.urls import path
from .views import Register, VerifyCode, Login, Logout

app_name = 'accounts'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('verify/', VerifyCode.as_view(), name='verify_code'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
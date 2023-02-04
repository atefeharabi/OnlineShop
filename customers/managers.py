from django.contrib.auth.models import BaseUserManager


class CustomerManager(BaseUserManager):
    def create_user(self, email, phone, password):
        if not email:
            raise ValueError('email field required')
        if not phone:
            raise ValueError('email field required')
        if not password:
            raise ValueError('email field required')
        customer = self.model(email=self.normalize_email(email), phone=phone)
        customer.set_password(password)
        customer.save(using=self.db)
        return customer


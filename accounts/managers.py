from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
        Create custom manager for User model
    """
    def create_user(self, email, phone, password):
        """
            customizing create_user statement
            :param email:
            :param phone:
            :param password:
            :return:
        """
        if not email:
            raise ValueError('email field required')
        if not phone:
            raise ValueError('email field required')
        if not password:
            raise ValueError('email field required')
        user = self.model(email=email, phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password):
        """
        customizing create_superuser statement
        :param email:
        :param phone:
        :param password:
        :return:
        """
        if not email:
            raise ValueError('email field required')
        if not phone:
            raise ValueError('email field required')
        if not password:
            raise ValueError('email field required')
        user = self.model(email=email, phone=phone)
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user

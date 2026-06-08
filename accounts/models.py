from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User Model
    Future fields:
        phone_number
        profile_picture
        address
    """
    pass

"Модель профиля пользователя"

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    "User's Profile data"
    bio = models.TextField(verbose_name="Biography")
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile", verbose_name="User"
    )
    birth_date = models.DateField(verbose_name="Birth date")
    avatar = models.ImageField(verbose_name="Avatar", upload_to="avatars/", default="avatar.png")

    class Meta:
        "Meta data"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

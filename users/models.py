"""Users Model."""
#Django
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """Profile model

    Proxy model that extends the base data with
    other information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return username."""
        return self.user.username
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import *
import uuid                                        # this is a unique id used each time user wants to reset id


# Create your models here.
class Password_Reset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}" 
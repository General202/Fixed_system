from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    patronymic = models.CharField("По-батькові", max_length=150, blank=True)
    battalion_number = models.CharField("Номер батальйону/підрозділу", max_length=50, blank=True)
    is_officer = models.BooleanField("Працівник поліції", default=False)

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.username})"
    
class AccessCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    is_used = models.BooleanField(default=False)
    issued_to = models.CharField(max_length=100, blank=True, null=True)  # необов’язково, щоб знати кому видали
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} ({'використано' if self.is_used else 'активний'})"
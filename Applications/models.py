from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmployeeDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} / {self.user.username}"
    
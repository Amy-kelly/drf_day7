from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=11,unique=True)

    class Meta:
        db_table = "admin_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class Coffee(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    kinds = models.CharField(max_length=32,verbose_name="种类")

    class Meta:
        db_table = "tb_coffee"
        verbose_name = "咖啡"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

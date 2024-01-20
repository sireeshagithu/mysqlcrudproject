from django.db import models

# Create your models here.
class User(models.Model):
    uname=models.CharField(max_length=50)
    uemail=models.EmailField(max_length=35)
    upassword=models.CharField(max_length=45)

    class Meta:
        db_table='users'
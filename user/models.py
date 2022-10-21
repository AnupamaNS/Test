from django.db import models

# Create your models here.
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    contact = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'

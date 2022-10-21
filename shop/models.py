from django.db import models

# Create your models here.
class Shop(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=50)
    u_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=112)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'shop'

from django.db import models

# Create your models here.
class Category(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'category'

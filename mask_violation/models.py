from django.db import models

# Create your models here.
class MaskViolation(models.Model):
    v_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table='mask_violation'
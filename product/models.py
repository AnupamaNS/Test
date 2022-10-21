from django.db import models

# Create your models here.
class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=50)
    price = models.CharField(max_length=112)
    c_id = models.CharField(max_length=11)
    qty = models.IntegerField()

    # c=models.ForeignKey('Category',to_fields='c_id',on_delete=models.CASCADE)
    s_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product'

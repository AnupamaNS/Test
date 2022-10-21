from django.db import models
from shop.models import Shop
from user.models import User
# Create your models here.
# class Rating(models.Model):
#     r_id = models.AutoField(primary_key=True)
#     # u_id = models.IntegerField()
#     u=models.ForeignKey(User,to_fields='u_id',on_delete=models.CASCADE)
#     ratin = models.IntegerField()
#     time = models.TimeField()
#     date = models.DateField()
#
#     class Meta:
#         managed = False
#         db_table = 'ratin'

# class Rating(models.Model):
#     r_id = models.AutoField(primary_key=True)
#     u_id = models.IntegerField()
#     rating = models.IntegerField()
#     time = models.TimeField()
#     date = models.DateField()
#
#     class Meta:
#         managed = False
#         db_table = 'ratin'

class Rating(models.Model):
    r_id = models.AutoField(primary_key=True)
    # u_id = models.IntegerField()
    u=models.ForeignKey(User,to_field='u_id',on_delete=models.CASCADE)
    rating = models.IntegerField()
    time = models.TimeField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'rating'

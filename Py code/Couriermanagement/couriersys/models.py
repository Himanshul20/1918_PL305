from django.db import models

# Create your models here.
SHIP_TYPE = (
    ('type','TYPE'),
    ('parcel','PARCEL'),
    ('document', 'DOCUMENT'),

)


class Booking(models.Model):
    AWB = models.IntegerField()
    sfname = models.CharField(max_length=20)
    slname = models.CharField(max_length=20)
    streetadd = models.CharField(max_length=30)
    streetadd2 = models.CharField(max_length=30)
    scity = models.CharField(max_length=20)
    sstate = models.CharField(max_length=20)
    scountry = models.CharField(max_length=20)
    spostal = models.IntegerField()
    smobile= models.IntegerField()
    Rfname = models.CharField(max_length=20)
    Rlname = models.CharField(max_length=20)
    Rstreetadd = models.CharField(max_length=30)
    Rstreetadd2 = models.CharField(max_length=30)
    Rcity = models.CharField(max_length=20)
    Rstate = models.CharField(max_length=20)
    Rcountry = models.CharField(max_length=20)
    Rpostal = models.IntegerField()
    Rmobile = models.IntegerField()
    weight = models.FloatField()
    shiptype = models.CharField(max_length=10,choices=SHIP_TYPE, default='type')
    cost = models.FloatField()

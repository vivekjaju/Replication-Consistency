from django.db import models

class Order(models.Model):
  fname = models.CharField(max_length=25)
  ldate = models.CharField(max_length=25)
  addr = models.CharField(max_length=250)
  num = models.IntegerField()
  bill = models.IntegerField()


class Order_copy(models.Model):
  fname = models.CharField(max_length=25)
  ldate = models.CharField(max_length=25)
  addr = models.CharField(max_length=250)
  num = models.IntegerField()
  bill = models.IntegerField()

  
  
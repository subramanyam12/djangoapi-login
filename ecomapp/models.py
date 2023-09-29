
from django.db import models
from django.contrib.auth.models import User



class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id=models.PositiveIntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    image=models.ImageField()
    price=models.PositiveIntegerField()
    discountprice=models.PositiveIntegerField()
    def __str__(self):
        return self.title


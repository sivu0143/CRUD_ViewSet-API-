from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    Categoryname=models.CharField(max_length=100,primary_key=True)
    CategoryID=models.IntegerField()
    def __str__(self):
        return self.Categoryname
class Product(models.Model):
    Categoryname=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    pid=models.IntegerField(primary_key= True)
    prdouctname=models.CharField(max_length=30)
    price=models.IntegerField()
    date=models.DateField()

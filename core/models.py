from django.db import models

# class Product is a product table in db

class Product(models.Model):
    title=models.CharField(max_length=200) #title varchar(200)
    price=models.DecimalField(max_digits=10,decimal_places=2) #price decimal(10)
    description=models.TextField(blank=True) # description TEXT, nullable

    class Meta:
        db_table = 'product'


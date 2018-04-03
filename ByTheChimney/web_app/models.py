from django.db import models

# Create your models here.

# Inventory as of 4/2/2018
# Mermaid		|	3 (S/M/L)		    |	20/22/26
# Dino 	 	    |	1 size			    |	22
# dog toys 	    |	2 types (3/4 braid)	|	1/2
# cat toys	    |	1 type			    |	1
# capes		    |	1 size			    |	20
# tutu          |   1 size              |   10
# special orders for capes available
class Product(models.Model):
    product = models.CharField(max_length=30)
    size = models.CharField(max_length=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    model = models.CharField(max_length=20)

class Purchase(models.Model):
    DateOfPurchase = models.DateTimeField()
    Location = models.CharField(max_length=30)
    SpecialEvent = models.BooleanField()
    CustomerName = models.CharField(max_length=50)

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)    
    price = models.DecimalField(max_digits=6, decimal_places=2)
    refunded = models.BooleanField()
    dateOfRefund = models.DateTimeField()

    
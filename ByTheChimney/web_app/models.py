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

products = ('Mermaid Tail', 'Dinosaur Tail', 'Dog Toy', 'Cat Toy', 'Cape', 'Tu-Tu')
sizes = ('S', 'M', 'L')
models = ('3-braid', '4-braid')

class Product(models.Model):
    product = models.CharField(max_length=30, choices=products)
    size = models.CharField(max_length=1, choices=sizes)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    model = models.CharField(max_length=20, choices=models)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    DateOfPurchase = models.DateTimeField()
    Location = models.CharField(max_length=30)
    SpecialEvent = models.BooleanField()
    CustomerName = models.CharField(max_length=50)

    def __str__(self):
        return (self.CustomerName + self.DateOfPurchase.strftime('%Y-%m-%d %H:%M'))

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)    
    price = models.DecimalField(max_digits=6, decimal_places=2)
    refunded = models.BooleanField()
    dateOfRefund = models.DateTimeField()

    
from django.db import models
from datetime import *

# Inventory as of 4/20/2018
# Mermaid		|	3 (S/M/L)		    |	20/22/26        <-Hanging, 8x11 sign
# Dino 	 	    |	1 size			    |	22              <-Hanging, 8x11 sign
# dog toys 	    |	2 types (3/4 braid)	|	1/2             <-Table, 4x6 sign
# cat toys	    |	1 type			    |	1               <-Table, 4x6 sign
# capes		    |	1 size			    |	20              <-Hanging, 8x11 sign
# dogs capes	|	1 size			    |	8               <-Table, 4x6 sign
# tutu          |   1 size              |   10              <-Hanging, 8x11 sign, 
# special orders for capes available
class Product(models.Model):
    products = (
        ('Mermaid Tail', 'Mermaid Tail'), 
        ('Dinosaur Tail', 'Dinosaur Tail'), 
        ('Dog Toy', 'Dog Toy'), 
        ('Cat Toy', 'Cat Toy'), 
        ('Cape', 'Cape'), 
        ('Dog Cape', 'Dog Cape'), 
        ('Tu-Tu', 'Tu-Tu'),
    )

    sizes = (
        ('S', 'Small'), 
        ('M', 'Medium'), 
        ('L', 'Large'),
    )

    toyModels = (
        ('3-braid', '3-braid'), 
        ('4-braid', '4-braid'),
    )

    product = models.CharField(max_length=30, choices=products)
    size = models.CharField(max_length=1, choices=sizes)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    model = models.CharField(max_length=20, choices=toyModels)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    DateOfPurchase = models.DateTimeField()
    Location = models.CharField(max_length=30)
    SpecialEvent = models.BooleanField()
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50, default="Anon")

    def __str__(self):
        return (self.CustomerName + self.DateOfPurchase.strftime('%Y-%m-%d %H:%M'))

    @property
    def full_name(self):
        #Returns the person's full name.
        return '%s %s' % (self.first_name, self.last_name)

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)    
    price = models.DecimalField(max_digits=6, decimal_places=2)
    refunded = models.BooleanField()
    dateOfRefund = models.DateTimeField()

    def __str__(self):
        return '%s, %s' (self.product, str(self.price))

class Event(models.Model):
    name = models.CharField(max_length=50)
    recurring = models.BooleanField()
    location = models.CharField(max_length=75)
    date = models.DateTimeField(default=datetime.now, blank=True)
    createDate = models.DateTimeField()
    rainDate = models.DateTimeField()
    isDelayed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def getUpcoming(self):
        return null



    
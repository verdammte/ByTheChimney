from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Purchase)
admin.site.register(Product)
admin.site.register(Transaction)
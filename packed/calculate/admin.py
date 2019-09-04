from django.contrib import admin

# Register your models here.
from .models import (Product, Box, invoice)


admin.site.register(Product)
admin.site.register(Box)
admin.site.register(invoice)


# Register your models here.

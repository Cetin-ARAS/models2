from django.contrib import admin
from .models import (
    Profile,
    Adress,
    Product
)

admin.site.register(Profile)
admin.site.register(Adress)
admin.site.register(Product)

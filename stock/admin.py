from django.contrib import admin
from .models import Product, StockTransaction, StockTransactionDetail

admin.site.register(Product)
admin.site.register(StockTransaction)
admin.site.register(StockTransactionDetail)

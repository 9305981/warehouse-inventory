from django.db import models

# Table 1: Product Master (prodmast)
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Table 2: Transaction Main (stckmain)
class StockTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    ]

    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.date.strftime('%Y-%m-%d %H:%M')}"

# Table 3: Transaction Details (stckdetail)
class StockTransactionDetail(models.Model):
    transaction = models.ForeignKey(StockTransaction, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} ({self.quantity}) in {self.transaction}"

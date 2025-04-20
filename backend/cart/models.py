from django.db import models

# Create your models here.
from django.db import models
from users.models import User  # assuming you're using a custom User model
from products.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Ensures one entry per product per user

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"

    def get_total_price(self):
        return self.quantity * self.product.price

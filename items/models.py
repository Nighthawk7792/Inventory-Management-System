from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator

class Item(models.Model):
    # Required Fields
    name = models.CharField(
        max_length=100,
        verbose_name="Item Name",
        help_text="Enter the item name (max 100 characters)"
    )
    
    description = models.TextField(
        blank=True,
        verbose_name="Description",
        help_text="Optional item description"
    )
    
    quantity = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Quantity in Stock",
        help_text="Current inventory count (must be 0 or greater)"
    )
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Unit Price",
        help_text="Price per unit (USD)"
    )
    
    # Automatic Fields
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date Created"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Updated"
    )
    
    # Optional Fields (uncomment if needed)
    # sku = models.CharField(
    #     max_length=50,
    #     unique=True,
    #     blank=True,
    #     null=True,
    #     verbose_name="SKU",
    #     help_text="Stock Keeping Unit"
    # )
    
    # category = models.ForeignKey(
    #     'Category',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )

    class Meta:
        ordering = ['-updated_at']  # Newest items first
        verbose_name = "Inventory Item"
        verbose_name_plural = "Inventory Items"
    
    def __str__(self):
        return f"{self.name} (ID: {self.id})"
    
    def get_absolute_url(self):
        return reverse('items:item_detail', kwargs={'pk': self.pk})
    
    @property
    def inventory_value(self):
        """Calculate total inventory value for this item"""
        return self.quantity * self.price

# Example Category model (uncomment if needed)
# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(blank=True)
#    
#     def __str__(self):
#         return self.name
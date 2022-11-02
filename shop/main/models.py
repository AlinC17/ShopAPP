from django.db import models

# Create your models here.


class ShopItems(models.Model):
    item_name = models.CharField(max_length=100, null=False, blank=False)
    item_price = models.FloatField(null=False)
    item_author = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateField(auto_now_add=True, editable=False)

class Image(models.Model):
    shop_item = models.ForeignKey(ShopItems, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField()

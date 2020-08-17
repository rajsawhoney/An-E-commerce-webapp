from django.db import models

# Create your models here.


class Offer(models.Model):
    occasion = models.CharField(("Occasion"), max_length=255)
    category = models.ForeignKey("product.Category", verbose_name=(
        "Offers On"), related_name='offers', on_delete=models.CASCADE)
    discount = models.IntegerField()
    limited_for = models.CharField(
        ("'Example: 2020-02-14 00:00:00'"), max_length=50)

    def __str__(self):
        return self.occasion

from django.db import models

# Create your models here.
class ProductTag(models.Model):
    title=models.CharField(max_length=100)
    product= models.ManyToManyField("product.Product", verbose_name=("Tags on:"),blank=True)
    tagged_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


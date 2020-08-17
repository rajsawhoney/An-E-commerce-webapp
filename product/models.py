from django.db.models.signals import pre_save, post_save

from utils.slugify_unique import unique_slug_generator
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.


class ProductManager(models.Manager):
    def get_category(self, pro_tag, category):
        return Product.objects.filter(product_tag=pro_tag).distinct().filter(category__name__icontains=category)


class Category(models.Model):

    categories = [
        ('LAPTOP', 'LAPTOP'),
        ('SMARTPHONE', 'SMARTPHONE'),
        ('CAMERA', 'CAMERA'),
        ('ACCESSORIES', 'ACCESSORIES'),
        ('NONE', ''),
    ]

    name = models.CharField(
        max_length=15, choices=categories, default='ACCESSORIES')
    description = models.TextField()
    background_image = models.ImageField(
        _("background_category_image"), upload_to='category_images', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product:category_view", kwargs={"slug": self.name})

    # def get_absolute_url(self):
    #     return f"categorical/{self.name}"


class ProductType(models.Model):

    name = models.CharField(max_length=128)
    has_variants = models.BooleanField(default=True)
    is_shipping_required = models.BooleanField(default=True)
    is_digital = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def is_digital(self):
        return self.is_digital


def set_thumbnail_name(instance, filename):
    title = instance.name
    slug = slugify(title)
    return "product_thumnails/%s-%s" % (slug, filename)


def set_product_slug(instance):
    title = instance.name
    slug = slugify(title)
    return slug


class Product(models.Model):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

    product_tag_choices = (
        ('new', _("NEW")),
        ('top', _("TOP")),
        ('hot', _("HOT")),
    )

    name = models.CharField(max_length=128)
    product_count = models.IntegerField(_("Items left in Store"), default=1)
    product_type = models.ForeignKey(
        ProductType, related_name="products", on_delete=models.CASCADE
    )

    product_tag = models.CharField(
        _("Product Tag"), max_length=5, choices=product_tag_choices, default="NEW")

    thumbnail = models.ImageField(
        upload_to=set_thumbnail_name, blank=True)

    description = RichTextField()

    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    price_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2

    )

    old_price = models.DecimalField(
        max_digits=10,
        decimal_places=2, blank=True, default=50000
    )
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, default=0)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    charge_taxes = models.BooleanField(default=True)
    overall_rating = models.DecimalField(
        _("Average Product Rating:"), max_digits=2, decimal_places=1, default=0)
    slug = models.SlugField(null=True, blank=True)
    rating1count = models.IntegerField(_("Rating1"), default=0)
    rating2count = models.IntegerField(_("Rating2"), default=0)
    rating3count = models.IntegerField(_("Rating3"), default=0)
    rating4count = models.IntegerField(_("Rating4"), default=0)
    rating5count = models.IntegerField(_("Rating5"), default=0)

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse("product:detail_view", kwargs={"pk": self.slug})

    def __str__(self):
        return self.name

    def snippet(self):
        return str(self.description[300:400])

    def calculateRating(self, rating):
        if rating == '1':
            self.rating1count += 1

        elif rating == '2':
            self.rating2count += 1

        elif rating == '3':
            self.rating3count += 1

        elif rating == '4':
            self.rating4count += 1

        elif rating == '5':
            self.rating5count += 1

        if self.rating1count or self.rating2count or self.rating3count or self.rating4count or self.rating5count:  # Checks the division by zero exception

            self.overall_rating = (self.rating1count + 2*self.rating2count + 3*self.rating3count + 4*self.rating4count + 5*self.rating5count)/(
                self.rating1count + self.rating2count + self.rating3count + self.rating4count + self.rating5count)

            self.overall_rating = round(self.overall_rating)
            self.save()


def set_product_Image_name(instance, filename):
    title = instance.name
    slug = slugify(title)
    return "product_images/%s-%s" % (slug, filename)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', verbose_name=_(
        "Select Product"), on_delete=models.CASCADE)
    product_images = models.ImageField(
        upload_to=set_product_Image_name, verbose_name=_("product Images"))

    def __str__(self):
        return str(self.product_images)


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.discount = (instance.old_price -
                         instance.price_amount)*100/(instance.old_price)

    if instance.discount >= 20:
        instance.product_tag = 'hot'

    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# Alter the product model before actually saving the data into the db
pre_save.connect(product_pre_save_receiver, sender=Product)

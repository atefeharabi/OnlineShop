from django.db import models
from django.urls import reverse


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, db_index=True)
    manufacturer = models.CharField(max_length=250)
    slug = models.SlugField(max_length=500, db_index=True)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', default='products/static/products/images/Blank.jpg')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    expired = models.DateField(null=True, blank=True)
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE, null=True, blank=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    vote = models.IntegerField(default=0)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product-detail', args=[self.slug])

    @property
    def rating_percentage(self):
        # noinspection PyTypeChecker
        return (self.rate * 100) / 5

    @property
    def final_price(self):
        discount = Discount.objects.get(id=self.discount.id)
        if discount.discount_type == 'PE':
            d = float(self.price) * discount.percent / 100
            if d < discount.max_amount:
                res = float(self.price) - d
            else:
                res = self.price - discount.max_amount
        elif discount.discount_type == 'CA':
            res = float(self.price) - discount.amount
        else:
            res = self.price
        return res


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='categories/%y/%m/%d', default='products/static/products/images/Blank.jpg')
    sub_category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:category-detail', args=[self.slug])


class Discount(models.Model):
    DISCOUNT_TYPE = [('PE', 'Percent'), ('CA', 'Cache'), ('CO', 'Coupon')]
    discount_type = models.CharField(choices=DISCOUNT_TYPE, max_length=2)
    percent = models.IntegerField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    max_amount = models.FloatField(null=True, blank=True)
    coupon = models.CharField(max_length=10, unique=True, blank=True, null=True)
    coupon_used = models.BooleanField(default=False)

    # def __str__(self):
    def display(self):
        if self.discount_type == 'PE':
            res = f"{self.percent} percent-under {self.max_amount} $."
        elif self.discount_type == 'CA':
            res = f"{self.amount} $"
        else:
            res = f"coupon: {self.coupon}"
        return res


class Feature(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.description}"

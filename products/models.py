from django.db import models


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, db_index=True)
    manufacturer = models.CharField(max_length=250)
    slug = models.SlugField(max_length=500, db_index=True)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    expired = models.DateField(null=True, blank=True)
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Discount(models.Model):
    DISCOUNT_TYPE = [('PE', 'Percent'), ('CA', 'Cache'), ('CO', 'Coupon')]
    discount_type = models.CharField(choices=DISCOUNT_TYPE, max_length=2)
    percent = models.IntegerField()
    amount = models.FloatField()
    max_amount = models.FloatField()
    coupon = models.CharField(max_length=10, unique=True)

    # @property
    # def percent(self):
    #     if self.discount_type == 'PE':
    #         return self.percent
    #     else:
    #         return 0
    #
    # @property
    # def amount(self):
    #     if self.discount_type == 'CA':
    #         return self.amount
    #     else:
    #         return 0
    def __str__(self):
        if self.discount_type == 'PE':
            res = f"{self.percent} percent-under {self.max_amount}."
        elif self.discount_type == 'CA':
            res = f"{self.amount} cashe discount."
        else:
            res = f"coupon: {self.coupon}"
        return res


class Feature(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.description}"

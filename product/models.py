from django.db import models
from django.core.urlresolvers import reverse

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits = 19, decimal_places = 2)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})

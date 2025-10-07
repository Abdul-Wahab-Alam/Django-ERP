from django.db import models

class Inventory(models.Model):
    product_id = models.AutoField(default=1)
    product_name = models.CharField()

    def __str__(self):
        return self.product_name
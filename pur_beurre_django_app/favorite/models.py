from django.db import models


class Favorite(models.Model):

    class Meta:
        unique_together = (('account_id', 'product_id', 'substitute_id'),)

    account_id = models.IntegerField(null=True)
    product_id = models.IntegerField(null=True)
    substitute_id = models.IntegerField(null=True)
    creating_date = models.DateTimeField(auto_now_add=True)

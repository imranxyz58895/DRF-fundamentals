from django.db import models


class Celebrity(models.Model):
    unique_no = models.IntegerField()
    name = models.CharField(max_length=200)
    net_worth = models.FloatField()
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Celebrity'
        verbose_name_plural = 'Celebrities'
    
    def __str__(self):
        return self.name 
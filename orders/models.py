from django.db import models

# Create your models here.
class Order(models.Model):

    company_name = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.company_name

    def json_object(self):
    	data = {'company_name': self.company_name, 'quantity': self.quantity}
    	return str(data)
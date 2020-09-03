from django.db import models


class Device(models.Model):
    CHOICE = (
        ('AVAILABLE', ' Item ready to sale'),
        ('SOLD', 'Item is not available'),
        ('RESTOCKING', 'Item is is added within few days')
    )

    type = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=0)

    status = models.CharField(max_length=10, choices=CHOICE, default='SOLD')
    issues = models.CharField(max_length=100, default='No issues')

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0}, Price : {1}'.format(self.type, self.price)


class Laptop(Device):
    pass


class Desktop(Device):
    pass


class Mobile(Device):
    pass

from django.db import models


class Trial(models.Model):

    year = models.IntegerField()
    month = models.IntegerField()
    temp = models.DecimalField(decimal_places=2, max_digits=4)
    fall = models.IntegerField()

    def __str__(self):
        return str(self.month)+'/'+str(self.year)

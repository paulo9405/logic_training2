from django.db import models

class DoubleSave(models.Model):
    value = models.IntegerField()
    double_value = models.IntegerField(blank=True, default=0)

    def save(self, *args, **kwargs):
        self.double_value = self.value * 2

        return super(DoubleSave, self).save(*args, **kwargs)



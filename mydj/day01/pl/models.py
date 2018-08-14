from django.db import models

# Create your models here.
class Bcyy(models.Model):
    name=models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    heat=models.IntegerField(
        default=50
    )
    def __str__(self):
        return self.name
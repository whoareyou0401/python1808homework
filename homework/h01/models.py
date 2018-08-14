

from django.db import models

# Create your models here.
class tea(models.Model):
    name=models.CharField(
        max_length=30
    )
    age=models.IntegerField(
        max_length=30,
        default=18
    )
# class teacher(models.Model):
#     name=models.CharField(
#         max_length=30
#     )
#     age=models.IntegerField(
#         max_length=30,
#         default=18
#     )
#     date=models.DateTimeField(
#         auto_now_add=True
#     )
#     # def __str__(self):
#     #     return self.name+str(self.age)
#     class Meta:
#         db_table="Teachers"

from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    age = models.IntegerField(
        verbose_name="年龄"
    )
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="身高"
    )
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="体重"
    )
    birthday = models.DateField(
        auto_now_add=True,
        verbose_name="出生日期"
    )
    school_state = models.BooleanField(
        default=True,
        verbose_name="是否在上学"
    )
    def __str__(self):
        return self.name+ '的年龄是:' + str(self.age)

    class Meta:
        db_table = 'Person'
        verbose_name = "人类"
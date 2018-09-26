from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(
        max_length=22,
        verbose_name="名字"
    )
    profrssion = models.CharField(
        max_length=22,
        verbose_name="职业"
    )
    power = models.IntegerField(
        verbose_name="战斗力",
        default=8000,
        db_column="hero_power"
    )
    birth_date = models.DateField(
        auto_now=True,
        verbose_name="出生日期"
    )
    last_date = models.DateField(
        auto_now=True,
        verbose_name="消失日期"
    )
    is_used = models.BooleanField(
        default=True,
        verbose_name="是否飞升"
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="英雄类"
        db_table="飞升战力表"

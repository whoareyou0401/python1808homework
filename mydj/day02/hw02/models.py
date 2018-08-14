from django.db import models

# Create your models here.

class Tvideo(models.Model):
    name=models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    playno=models.IntegerField(
        verbose_name="播放量",
        default=100

    )
    birthday=models.DateTimeField(
        auto_now_add=True,
        verbose_name="投稿时间",
        db_column="uday"
    )
    def __str__(self):
        return self.name+str(self.playno)
    class Meta:
        verbose_name="视频类"
        db_table="u_video"


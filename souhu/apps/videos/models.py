from django.db import models

# Create your models here.
class News_video(models.Model):
    news_from=models.CharField(max_length=10)
    release_date = models.DateField(verbose_name='发布日期')
    video=models.CharField(max_length=1000,verbose_name="视频内容")


    class Meta:
        app_label = 'videos'
        db_table = 'tb_news_video'
        verbose_name = '新闻视频'
        verbose_name_plural = verbose_name
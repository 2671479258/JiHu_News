from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=50,verbose_name='标题')
    content=models.CharField(max_length=600,verbose_name='内容')
    release_date=models.DateField(verbose_name='发布日期')

    class Meta:
        app_label = 'article'
        db_table = 'tb_articles'
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title



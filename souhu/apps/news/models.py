from django.db import models

# Create your models here.

class News_content(models.Model):
    news_from=models.CharField(max_length=10)
    release_date = models.DateField(verbose_name='发布日期')
    character1=models.CharField(max_length=1000,verbose_name="第一大段")
    img1=models.ImageField(max_length=200,default='',null=True,verbose_name='图片1')
    tag1=models.CharField(max_length=50,null=True,default='')
    character2 = models.CharField(max_length=1000, verbose_name="第二大段",null=True)
    img2 = models.ImageField(max_length=200, default='', null=True, verbose_name='图片2')
    tag2 = models.CharField(max_length=50, null=True, default='')
    character3 = models.CharField(max_length=1000, verbose_name="第三大段", null=True)
    img3 = models.ImageField(max_length=200, default='', null=True, verbose_name='图片3')
    tag3 = models.CharField(max_length=50, null=True, default='')
    character4 = models.CharField(max_length=1000, verbose_name="第四大段", null=True)

    class Meta:
        app_label = 'news'
        db_table = 'tb_news_content'
        verbose_name = '新闻内容'
        verbose_name_plural = verbose_name


from videos.models import News_video

class News(models.Model):
    title=models.CharField(max_length=50,verbose_name='标题')
    default_image = models.ImageField(max_length=200, default='', null=True, blank=True, verbose_name='默认图片')
    release_date=models.DateField(verbose_name='发布日期')
    detail=models.ForeignKey(News_content,on_delete=models.CASCADE,null=True)
    video_detail = models.ForeignKey(News_video, on_delete=models.CASCADE, null=True)




    class Meta:
        app_label = 'news'
        db_table = 'tb_news'
        verbose_name = '新闻管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

from users.models import User
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    new=models.ForeignKey(News,on_delete=models.CASCADE,null=True)
    release_date = models.DateTimeField(verbose_name='发布日期',null=True)
    comment=models.CharField(max_length=300)

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies_sent', null=True)
    release_date = models.DateTimeField(verbose_name='发布日期', null=True)
    reply = models.CharField(max_length=300)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies_received', null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'news'
        db_table = 'tb_reply'
        verbose_name = '回复管理'
        verbose_name_plural = verbose_name
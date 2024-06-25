from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile = models.CharField(max_length=11,unique=True)
    real_name=models.CharField(max_length=10,null=True,verbose_name='真名')
    profile=models.CharField(max_length=200,default='http://127.0.0.1:8080/images/profile/default.jpg')
    area=models.CharField(max_length=10,null=True)

    class Meta:
        app_label = 'users'
        db_table='tb_users'
        verbose_name='用户管理'
        verbose_name_plural=verbose_name

    def set_password(self, raw_password):
        # 存储密码为明文形式
        self.password = raw_password

    def check_password(self, raw_password):
        # 直接比较密码明文
        return self.password == raw_password

    def save(self, *args, **kwargs):
        # 如果需要保存实例时进行其他操作，可以在这里添加
        super().save(*args, **kwargs)

    def __str__(self):
        return self.real_name

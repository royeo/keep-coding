from django.db import models
from django.contrib.auth.models import User


# 帖子表
class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey('BBSUser')  # 外键是一对多
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title


# 主题表
class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    administrator = models.ForeignKey('BBSUser')


# 用户表
class BBSUser(models.Model):
    user = models.OneToOneField(User)  # OneToOne是一对一
    signature = models.CharField(max_length=128, default='This guy is too lazy to leave anything here')
    photo = models.ImageField(upload_to='upload_img/', default='upload_img/user_head.jpg')  # upload_to：自动创建upload_img目录

    def __str__(self):
        return self.user.username



















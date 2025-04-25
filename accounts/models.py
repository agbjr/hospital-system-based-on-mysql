from django.db import models

class User(models.Model):
    userName = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'  # 显式绑定到数据库中的 user 表

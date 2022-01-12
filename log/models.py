from django.db import models

# Create your models here.

class person(models.Model):
    TITLE_OPTIONS = [
    (0, '行政人員'),
    (1, '正式教師'),
    (2, '代理教師'),
    (3, '兼任教師'),
    ]

    title = models.IntegerField(
              '身分', 
              default=0, 
              choices=TITLE_OPTIONS
           )
    JOB_OPTIONS = [
    (0, '國中部'),
    (1, '高中部'),
    ] 
    name = models.CharField('借用人', max_length=10)
    subject = models.CharField('科目', max_length=10)
    job_title = models.CharField('職稱', max_length=10)
    telephone = models.CharField('連絡電話', max_length=10)
    email = models.CharField('電子郵件', max_length=10)
    
    SITUATION_OPTIONS = [
    (0, '工作中'),
    (1, '已離職'),
    ]

    situation = models.IntegerField(
              '狀態', 
              default=0, 
              choices=SITUATION_OPTIONS
           )
class number(models.Model):
    number = models.CharField('設備型號', max_length=10)
    #接下來 是購置日期
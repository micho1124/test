# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class Thread(models.Model):
    #タイトル
    title = models.CharField(u'タイトル', max_length=200, blank=False)
    #メッセージ
    message = models.TextField(u'メッセージ', blank=False)
    #登録日時
    pub_date = models.DateTimeField(u'登録日時', auto_now_add=True, editable=False)
    
    class Meta:
        verbose_name = u'スレッド'
    
    def __unicode__(self):
        return self.message

class Comment(models.Model):
     #スレッド
     thread = models.ForeignKey(Thread, verbose_name=u'スレッド')
     #メッセージ
     message = models.CharField(u'メッセージ', max_length=200, blank=False)
     #登録日時
     pub_date = models.DateTimeField(u'登録日時', auto_now_add=True, editable=False)
     class Meta:
        verbose_name = u'コメント'
     def __unicode__(self):
        return self.message

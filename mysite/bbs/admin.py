# -*- coding: utf-8 -*-
from django.contrib import admin
from mysite.bbs.models import Thread, Comment

class CommentInline(admin.StackedInline):
	model = Comment
        extra = 1

class ThreadAdmin(admin.ModelAdmin):
	inlines = [CommentInline]

admin.site.register(Thread, ThreadAdmin)

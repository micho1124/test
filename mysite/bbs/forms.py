# -*- coding: utf-8 -*-
from django.forms import ModelForm
from mysite.bbs.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ('thread', )

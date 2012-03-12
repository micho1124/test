# Create you# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from mysite.bbs.models import Thread, Comment
from mysite.bbs.forms import CommentForm
#####
#from django import forms
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
#####

def thread_detail(request, thread_id):
    '''
    指定したスレッドを表示する。
    @param thread_id: スレッドID
    '''  
    #表示するスレッド       
    thread = get_object_or_404(Thread, pk=thread_id)
    #コメントの登録処理
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #コメントを登録
            comment = form.save(commit = False)
            comment.thread = thread
            comment.save()
            form = CommentForm() #フォームの初期化
            return HttpResponseRedirect('')
    else:            
        form = CommentForm()
    #スレッドのコメント
    comment_list = thread.comment_set.all().order_by('id')
    return render_to_response('bbs/thread_detail.html',
                              {'thread': thread,
                               'comment_list': comment_list,
                               'form': form})

def success(request):
    return render_to_response('bbs/thread_success.html',
                              {"suc": "投稿が完了しました"})

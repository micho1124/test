###coding=utf-8###

from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from mysite.bbs.models import Thread
import mysite.bbs.views
admin.autodiscover()


#urlpatterns = patterns('',
#     url(r'^admin/', include(admin.site.urls)),
#)


#urlpatterns = patterns('',
#    url(r'^admin/', include(admin.site.urls)),
#    #スレッド一覧のページ
#    (r'^(?P<page>[0-9]+)/$',
#     'django.views.generic.list_detail.object_list',
#     {'queryset': Thread.objects.all().order_by('-id'),
#      'paginate_by': 5,
#      'allow_empty': True}),
#    #トップページ。スレッド一覧のページにリダイレクトする
#    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/1/'}),
#)

#urlpatterns = patterns('',
#    url(r'^admin/', include(admin.site.urls)),
#    #スレッド一覧のページ
#    (r'^(?P<page>[0-9]+)/$',
#     'django.views.generic.list_detail.object_list',
#     {'queryset': Thread.objects.all().order_by('-id'),
#      'paginate_by': 5,
#      'allow_empty': True}),
#    #トップページ。スレッド一覧のページにリダイレクトする
#    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/1/'}),
#    #スレッドの新規作成ページ
#    (r'^thread/new/$',
#     'django.views.generic.create_update.create_object',
#     {'model': Thread,
#     'post_save_redirect': ''}),
#)


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #スレッド一覧のページ
    (r'^(?P<page>[0-9]+)/$',
     'django.views.generic.list_detail.object_list',
     {'queryset': Thread.objects.all().order_by('-id'),
      'paginate_by': 5,
      'allow_empty': True}),
    #トップページ。スレッド一覧のページにリダイレクトする
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/1/'}),
    #スレッドの新規作成ページ
    (r'^thread/new/$',
     'django.views.generic.create_update.create_object',
     {'model': Thread,
     'post_save_redirect': '/success/'}),
    #スレッドの詳細ページ
    (r'^thread/(?P<thread_id>\d+)/$', 'bbs.views.thread_detail'),
    #投稿完了
    (r'^success/$', 'bbs.views.success'),
    ###
    #画像表示の設定
    #
    (r'^images_site/(?P<path>.*)$','django.views.static.serve', dict(document_root=settings.MEDIA_ROOT)),    
    #
    
)

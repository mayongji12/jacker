from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from app01 import views
from rest_framework import routers, serializers,viewsets
router = routers.DefaultRouter()
router.register(r'configuration' , views.ConfigurationViewSet)
router.register(r'task_center' , views.TaskCenterViewSet)
router.register(r'host_profile' , views.HostProfileViewSet)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
	(r'^/$', views.index),
	(r'^account_login/$', views.account_login),
	(r'^dashboard/$', views.dashboard),
#	(r'^server_manager/$', server_manager),
	(r'^task_center/$', views.task_center),
	(r'^monitor/$', views.monitor),
	(r'^assets/$', views.assets),
	(r'^logout/$', views.logout),
#	(r'batch/$', batch),
#	(r'crontab/$', crontab),
#	(r'webshell/$', webshell),
#	(r'^server_manager/batch/$', batch),
#	(r'^server_manager/crontab/$', crontab),
#	(r'^server_manager/webshell/$', webshell),
#     url(r'^ajax_list/$', 'app01.views.ajax_list', name='ajax-list'),
     url(r'^cpu_idle/$', views.cpu_idle),
#     url(r'^ajax_dict/$', 'app01.views.ajax_dict', name='ajax-dict'),
#     url(r'^add/$', 'app01.views.add', name='add'),
     url(r'^ajax_swap_total/$', views.ajax_swap_total),
     url(r'^ajax_swap_used/$', views.ajax_swap_used),
#    url(r'^api/', include('api.urls')),
    (r'^graph/$', views.graph),
    (r'^$', views.index),
    (r'^new_task/$',views.new_task),
    (r'^task/detail/(\d+)/$',views.task_detail),
    (r'^task/task_logs/(\d+)/$', views.task_logs),
    (r'^task_center/$',views.task_center),
)

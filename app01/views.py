# Create your views here.
import os
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from rest_framework import viewsets
from rest_framework import status
from django.contrib import auth
#import sysdata
from django.core import serializers
import json
import models
import time,random
from rest_framework.response import Response
from rest_framework.decorators import api_view
import custom_forms
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render
from socketclient import *
from django.views.decorators.csrf import csrf_exempt
import cPickle as pickle
'''
#django before 1.7 can not support JsonResponse,so rewrite it.
class JsonResponse(HttpResponse):
    def __init__(self,
            content={},
            mimetype=None,
            status=None,
            content_type='application/json'):
 
        super(JsonResponse, self).__init__(
            json.dumps(content),
            mimetype=mimetype,
            status=status,
            content_type=content_type)
# Add by myj 20150730







def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def ajax_list(request):
    a = 9
    return HttpResponse(json.dumps(a), content_type='application/json')

def ajax_dict(request):
    name_dict = {'twz': 70}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')



def ajax_list(request):
    return HttpResponse(json.dumps(sysdata.cpuinfo()[0]), content_type='application/json')

def ajax_dict(request):
    return HttpResponse(json.dumps(sysdata.cpuinfo()[1]), content_type='application/json')
'''


#def ajax_list(request):
#    return HttpResponse(json.dumps(sysdata.cpuinfo()[0]), content_type='application/json')
'''
def cpu_idle(request):
    fi = file('tmp.pkl','wb')
    m_ip = "192.168.1.86"
    command = "psutil.cpu_times_percent(percpu=False)[3]"
#    print "json_cpu: ",json.dumps(sclient(m_ip,command))
    return HttpResponse(json.dumps(float(sclient(m_ip,command))), content_type='application/json')
'''
#@csrf_exempt
def cpu_idle(request):
    #if request.method=='POST':
        if request.POST.get('selecthost'):
            selecthost = request.POST.get('selecthost')
            selectip = request.POST.get('selectip')
            selectitm = [selecthost,selectip]
            status_tag = "post_itm"
            f1 = open('tmp_cpu.pkl','wb')
            pickle.dump(selectitm,f1,True)
            f1.close()
#m_ip = "192.168.1.86"
            m_ip = selecthost
        else:
            f1 = open('tmp_cpu.pkl','rb')
            selectitm = pickle.load(f1)
            m_ip = selectitm[0] 
            selectip = selectitm[1]
#            selectitm = pickle.load(f1)
#            m_ip = selectitm[0]
#            selectip = selectitm[1]
#            m_ip = pickle.load(f1)[0]
#            print pickle.load(f1)
            #selectip = pickle.load(f1)[1]
            f1.close()
            status_tag = ""
        ip_list = models.Host.objects.all()
        json_dict = {}
        for ip in ip_list:
            m_ip = ip.ip
            print 'ip.ip:',ip.ip
            command = 'psutil.cpu_times_percent(percpu=False)[3]'
            cpupers = float(sclient(m_ip,command))
            print 'cpupers:',cpupers
            if cpupers:
                json_dict[m_ip] = cpupers
            else:
                json_dict[m_ip] = 'null'
        for k in json_dict:
            print "k:%s  json_dict:%s"%(k,json_dict[k]) 
     
        
        return HttpResponse(json.dumps((json_dict,selectip)),content_type='application/json')
 
#        command =selecthost received_json['selecthost']
#    print "json_cpu: ",json.dumps(sclient(m_ip,command))
'''
        datetime = int(time.time()*1000)
        cpupers = float(sclient(m_ip,command))
        f_cpu = open("%s_cpudate.txt" %m_ip,"ab")
        f_cpu_define = open("%s_cpudate.txt" %m_ip,"rb")
        if os.path.exists('%s_cpudate.txt' %m_ip):
            date_list = []
            for line in f_cpu_define.readlines():
                line = line.split(':')
                line[0] = int(line[0])
                line[1] = float(line[1])
                date_list.append(line)
            f_cpu.write('%s:%s\r\n' %(datetime,cpupers))
        else:
            for i in range(int(time.time()*1000 - 9),int(time.time()*1000 + 1)):
                f_cpu.write('%s:200\r\n' %i)
            date_list = []
            for line in f_cpu_define.readlines():
                line.split(':')
                line[0] = int(line[0])
                line[1] = float(line[1])
                date_list.append(line)
            f_cpu.write('%s:%s\r\n' %(datetime,cpupers))
        f_cpu_define.close()
        f_cpu.close()
#        f_cpu_define = 
#        f_cpu_define = pickle.load(f_cpu) 
#        print f_cpu_define
        return HttpResponse(json.dumps((json_dict,selectip,datetime,date_list)),content_type='application/json')

'''
#        return HttpResponse(json.dumps(sclient(m_ip,command)), content_type='application/json')

#def cpu_idle(request):
#    print "json_cpu: ",json.dumps(sysdata.cpuinfo()[0])
#    return HttpResponse(json.dumps(sysdata.cpuinfo()[0]), content_type='application/json')
#def cpu_used(request):
#    return HttpResponse(json.dumps(sysdata.cpuinfo()[1]), content_type='application/json')
#def ajax_mem_total(request):
#    return HttpResponse(json.dumps(sysdata.meminfo()[0]), content_type='application/json')
#
#def ajax_mem_used(request):
#    return HttpResponse(json.dumps(sysdata.meminfo()[1]), content_type='application/json')

#def ajax_swap_total(request):
#    return HttpResponse(json.dumps(sysdata.swapinfo()[0]), content_type='application/json')
@csrf_exempt
def ajax_swap_total(request):
        if request.POST.get('selecthost'):
            selecthost = request.POST.get('selecthost')
            f1 = open('tmp_st.pkl','wb')
            pickle.dump(selecthost,f1,True)
            f1.close()
            print selecthost
#        m_ip = "192.168.1.86"
            m_ip = selecthost
        else:
            f1 = open('tmp_st.pkl','rb')
            m_ip = pickle.load(f1)
            f1.close()
        command = "psutil.swap_memory().total/1024/1024"
        print long(sclient(m_ip,command))
        return HttpResponse(json.dumps(long(sclient(m_ip,command))), content_type='application/json')

#def ajax_swap_used(request):
#    return HttpResponse(json.dumps(sysdata.swapinfo()[1]), content_type='application/json')
@csrf_exempt
def ajax_swap_used(request):
        if request.POST.get('selecthost'):
            selecthost = request.POST.get('selecthost')
            f1 = open('tmp_su.pkl','wb')
            pickle.dump(selecthost,f1,True)
            f1.close()
            print selecthost
#        m_ip = "192.168.1.86"
            m_ip = selecthost
        else:
            f1 = open('tmp_su.pkl','rb')
            m_ip = pickle.load(f1)
            f1.close()
        command = "psutil.swap_memory().used/1024/1024"
        return HttpResponse(json.dumps(long(sclient(m_ip,command))), content_type='application/json')



def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))
@login_required
def dashboard(request):
#       form = custom_forms.DashboardForm()
#        form = custom_forms.DashboardForm()
        ip_list = models.Host.objects.all()
        print 'ip_list: ',ip_list
        list_ip = []
        for ip in ip_list:
            print 'ip:',ip,type(ip)
            list_ip.append((str(ip.ip)).replace('.','_'))
        print list_ip
#        monitor_ip = monitor_items.ip 
#        monitor_hosts = monitor_item.hosts
#        ip_hosts_dict = dict(map(lambda x,y:[x,y],monitor_ip,monitor_hosts))
	return render_to_response('dashboard.html',{'user':request.user,'ip_list':ip_list,'list_ip':list_ip},context_instance=RequestContext(request))
 
#def task_center(request):
#	ip_list = IP.objects.all()
#	return render_to_response('task_center.html',{'user':request.user,'ip_list':ip_list})
'''
def server_manager(request):
	ip_list = IP.objects.all()
	return render_to_response('server_manager.html',{'user':request.user,'ip_list':ip_list})
def batch(request):
  return render_to_response('server_manager/batch.html',{'user':request.user})

def crontab(request):
  return render_to_response('server_manager/crontab.html',{'user':request.user})
def webshell(request):
  return render_to_response('server_manager/webshell.html',{'user':request.user})
'''
@login_required
def monitor(request):
    return render_to_response('monitor.html',{'user':request.user},context_instance=RequestContext(request))
@login_required
#def assets(request):
#        ip_list = models.Host.objects.all()
#	return render_to_response('assets.html',{'user':request.user,'ip_list':ip_list},context_instance=RequestContext(request))

def assets(request):
#        type(data)
#        print data
#        ip_list = custom_forms.TaskCenterForm()
#        ip_list = models.Host.objects.all()
     #   json_data = json.loads(request.body)
#        json_data = simplejson.loads(request.raw_post_data)
#            json_data = request.POST.get('select')
	    return render_to_response('assets.html',{'user':request.user},context_instance=RequestContext(request))

def account_login(request):
	print "login ",request.POST
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = auth.authenticate(username= username, password=password)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/dashboard/')
	else:
		return render_to_response('index.html',{'login_err':"Wrong name or password!"},context_instance=RequestContext(request))


def logout(request):
	user = request.user
	auth.logout(request)
#	return HttpResponse("<h3>User %s logout!</h3>" % user)
	return render_to_response("index.html",context_instance=RequestContext(request))
'''
def batch(request):
	return render_to_response('/server_manager/batch.html',{'user':request.user})

def crontab(request):
	return render_to_response('/server_manager/crontab.html',{'user':request.user})

def webshell(request):
	return render_to_response('/server_manager/webshell.html',{'user':request.user})
'''



#############################cp from TriA##############################

import serializers
class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset =  models.Host.objects.all()
    serializer_class = serializers.HostSerializer 
    
def monitor_data(request):
    print request.POST 
    
    return HttpResponse('service sends status report success!!')


def graph(request):
    return render_to_response('index.htm')


def graph_data(request):
    '''fake_data = [[1230771600000, -5.8, 0.1],
        [1230858000000, -4.1, 1.4],
        [1230944400000, -0.5, 4.1],
        [1231030800000, -8.9, -0.7],
        [1231117200000, -9.7, -3.7],
        [1231203600000, -3.4, 3.2]]
    '''
    fake_data = []
    start_num = 86400
    for i in range(86400):
        point = [(time.time() -start_num)*1000, random.randrange(100) ]
        fake_data.append(point)
        start_num -=1
        
    
    return HttpResponse(json.dumps(fake_data))


###############below for task allocations #######################


class  TaskCenterViewSet(viewsets.ModelViewSet):
    #print self.REQUEST
    queryset = models.TaskCenter.objects.all()
    serializer_class = serializers.TaskCenterSerializer
    

class HostProfileViewSet(viewsets.ModelViewSet):
    queryset =  models.Host.objects.all()
    serializer_class = serializers.HostProfileSerializer     

@api_view(['GET'])
#def new_tasks(request,last_task_id):
def new_tasks(request):
        
#    query_set = models.TaskCenter.objects.filter(id__gt=last_task_id)
    print '---->',query_set
    serializer_class = serializers.TaskCenterSerializer(query_set,many=True)
    #return Response(serializer_class.data,status=status.HTTP_300_MULTIPLE_CHOICES)
    return Response(serializer_class.data)
@api_view(['POST'])
def task_result(request):       
    
    
    print request.POST 
    host_profile = json.loads(request.POST.get('host_profile'))
    task_status = request.POST.get('status')
    task_result = request.POST.get('run_log')
    task_profile = json.loads(request.POST.get('task'))
    
    host_profile = host_profile
    task_obj = models.TaskCenter.objects.get(id=task_profile.get('id'))
    models.TaskLog.objects.create(task=task_obj,
                                  result=task_status,
                                  log = task_result,
                                  host_id = host_profile.get('id')
                                  )
   
    
    return HttpResponse('...result submitted...')





###########below for web pages ###############


def task_center(request):
    form = custom_forms.TaskCenterForm()
    #task_list = models.TaskCenter.objects.all()
    task_list  = []
    
    for task in models.TaskCenter.objects.all():
        task_info = {'id':task.id,
                     'name':task.name,
                     'description':task.description,
                     'task_type':task.task_type,
                     'hosts':task.hosts,
                     'groups':task.groups,
                     'created_by':task.created_by,
                     'kick_off_at':task.kick_off_at,
                     'total_tasks':models.TaskLog.objects.filter(task_id=task.id).count(),
                     'failure':models.TaskLog.objects.filter(task_id=task.id,result='failed').count(),
                     'success':models.TaskLog.objects.filter(task_id=task.id,result='success').count(),
                     }
    
        task_list.append(task_info)
        print task_info['failure']
        print task_info['success']
    return render_to_response('task_center.html',{'user':request.user,'form':form,
                                            'task_list':task_list},context_instance=RequestContext(request))

@api_view(['POST'])
def new_task(request):
    
    form = custom_forms.TaskCenterForm(request.POST)
    print request.POST
    
    if form.is_valid():
        print 'form is valid'
        #form.cleaned_data['created_by'] = models.UserProfile.objects.all()[0]
        print  form.cleaned_data
        form.save()
        return HttpResponseRedirect('/task_center/')
    else:
        print form.errors
        return render_to_response('task_center.html',{'form':form},context_instance=RequestContext(request))

def task_detail(request,task_id):
    
    return render_to_response('task_detail.html',{'task_id':task_id})   


def task_logs(request,task_id):
    
    
    success_count = models.TaskLog.objects.filter(task_id=task_id,result='success').count()
    failure_count = models.TaskLog.objects.filter(task_id=task_id,result='failure').count()
    task_hosts = models.TaskCenter.objects.get(id=task_id).hosts.select_related()
    task_groups = models.TaskCenter.objects.get(id=task_id).groups.select_related()
    total_tasks = [] 
    total_tasks.extend(task_hosts) 
    
    for group in task_groups:
        total_tasks += models.Host.objects.filter(group__name = group.name)
    
    print total_tasks
    print set(total_tasks)
    log_list =[]
    for log in models.TaskLog.objects.filter(task_id=task_id):
        host = models.Host.objects.get(id=log.host_id)
        log_dic = {'result': log.result,
                   'log': log.log,
                   'host': host.hostname,
                   'ip': host.ip,
                   'date': log.date.strftime("%Y-%m-%d %H:%M:%S")}
        log_list.append(log_dic)
    
    task_detail = {'success_count': success_count,
                   'failure_count': failure_count,
                   'total_task': len(set(total_tasks)),
                   'log_list': log_list}
    
    return HttpResponse(json.dumps(task_detail))

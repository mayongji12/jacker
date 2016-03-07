# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=250)),
                ('recovery_notice', models.BooleanField(default=True)),
                ('recovery_subject', models.CharField(max_length=100)),
                ('recovery_message', models.CharField(max_length=250)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('data_type', models.CharField(default=b'char', max_length=32, verbose_name='\u6570\u636e\u7c7b\u578b')),
                ('threshold', models.CharField(max_length=64, verbose_name='\u9600\u503c')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Formulas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('key', models.CharField(unique=True, max_length=64)),
                ('memo', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Graphs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('graph_type', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('display_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(unique=True, max_length=50)),
                ('display_name', models.CharField(unique=True, max_length=50)),
                ('ip', models.IPAddressField(unique=True)),
                ('port', models.IntegerField(default=b'22')),
                ('os', models.CharField(default=b'linux', max_length=20, verbose_name=b'Operating System')),
                ('status_monitor_on', models.BooleanField(default=True)),
                ('snmp_on', models.BooleanField(default=True)),
                ('snmp_version', models.CharField(default=b'2c', max_length=10)),
                ('snmp_community_name', models.CharField(default=b'public', max_length=50)),
                ('snmp_security_level', models.CharField(default=b'auth', max_length=50)),
                ('snmp_auth_protocol', models.CharField(default=b'MD5', max_length=50)),
                ('snmp_user', models.CharField(default=b'triaquae_snmp', max_length=50)),
                ('snmp_pass', models.CharField(default=b'my_pass', max_length=50)),
                ('poll_interval', models.IntegerField(default=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('key', models.CharField(unique=True, max_length=100)),
                ('data_type', models.CharField(max_length=50, choices=[(b'float', b'Float'), (b'string', b'String'), (b'integer', b'Integer')])),
                ('unit', models.CharField(default=b'%', max_length=30)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('send_via', models.CharField(max_length=30, choices=[(b'email', b'Email'), (b'sms', b'SMS')])),
                ('notice_times', models.IntegerField(default=5)),
                ('notice_interval', models.IntegerField(default=300, verbose_name=b'notice_interval(sec)')),
                ('send_to_groups', models.ManyToManyField(to='app01.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operators',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('key', models.CharField(max_length=32)),
                ('memo', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=100)),
                ('host_status', models.CharField(default=b'Unkown', max_length=10)),
                ('ping_status', models.CharField(default=b'Unkown', max_length=100)),
                ('last_check', models.CharField(default=b'N/A', max_length=100)),
                ('host_uptime', models.CharField(default=b'Unkown', max_length=50)),
                ('attempt_count', models.IntegerField(default=0)),
                ('breakdown_count', models.IntegerField(default=0)),
                ('up_count', models.IntegerField(default=0)),
                ('snmp_alert_count', models.IntegerField(default=0)),
                ('availability', models.CharField(default=0, max_length=20)),
                ('host', models.OneToOneField(to='app01.Host')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('check_interval', models.IntegerField(default=300)),
                ('description', models.TextField()),
                ('conditons', models.ManyToManyField(to='app01.Conditions', null=True, verbose_name='\u9600\u503c\u5217\u8868', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('monitor_type', models.CharField(max_length=50, choices=[(b'agent', b'Agent'), (b'snmp', b'SNMP'), (b'wget', b'Wget')])),
                ('plugin', models.CharField(max_length=100)),
                ('item_list', models.ManyToManyField(to='app01.Items')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('task_type', models.CharField(max_length=32, verbose_name='\u4efb\u52a1\u7c7b\u578b', choices=[(b'cmd', b'\xe5\x91\xbd\xe4\xbb\xa4\xe6\x89\xa7\xe8\xa1\x8c'), (b'file_transfer', b'\xe6\x96\x87\xe4\xbb\xb6\xe5\x88\x86\xe5\x8f\x91'), (b'config_allocation', b'\xe9\x85\x8d\xe7\xbd\xae\xe4\xb8\x8b\xe5\x8f\x91')])),
                ('content', models.TextField(verbose_name='\u4efb\u52a1\u5185\u5bb9')),
                ('kick_off_at', models.DateTimeField(null=True, verbose_name='\u6267\u884c\u65f6\u95f4', blank=True)),
                ('memo', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.CharField(max_length=32, verbose_name='\u7ed3\u679c', choices=[(b'success', '\u6210\u529f'), (b'failed', '\u5931\u8d25'), (b'unknown', '\u672a\u77e5')])),
                ('log', models.TextField(verbose_name='\u4efb\u52a1\u65e5\u5fd7')),
                ('host_id', models.IntegerField(default=None, verbose_name='\u6c47\u62a5\u4e3b\u673aID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('task', models.ForeignKey(to='app01.TaskCenter')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('graph_list', models.ManyToManyField(to='app01.Graphs', null=True, blank=True)),
                ('service_list', models.ManyToManyField(to='app01.ServiceList')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrunkServers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('description', models.CharField(max_length=150, blank=True)),
                ('ip_address', models.IPAddressField()),
                ('port', models.IntegerField(default=9998)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='taskcenter',
            name='created_by',
            field=models.ForeignKey(verbose_name='\u4efb\u52a1\u521b\u5efa\u8005', blank=True, to='app01.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taskcenter',
            name='groups',
            field=models.ManyToManyField(default=None, to='app01.Group', verbose_name='\u9009\u62e9\u7ec4'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taskcenter',
            name='hosts',
            field=models.ManyToManyField(default=None, to='app01.Host', verbose_name='\u9009\u62e9\u4efb\u52a1\u4e3b\u673a'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicelist',
            name='service',
            field=models.ForeignKey(to='app01.Services'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='operations',
            name='send_to_users',
            field=models.ManyToManyField(to='app01.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='child_of',
            field=models.ForeignKey(blank=True, to='app01.TrunkServers', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='custom_services',
            field=models.ManyToManyField(to='app01.Services', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='group',
            field=models.ManyToManyField(to='app01.Group', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(blank=True, to='app01.Idc', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='template_list',
            field=models.ManyToManyField(to='app01.Templates', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='template_list',
            field=models.ManyToManyField(to='app01.Templates', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='graphs',
            name='datasets',
            field=models.ManyToManyField(to='app01.Items'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conditions',
            name='formula',
            field=models.ForeignKey(verbose_name='\u8fd0\u7b97\u51fd\u6570', blank=True, to='app01.Formulas', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conditions',
            name='item',
            field=models.ForeignKey(verbose_name='\u76d1\u63a7\u503c', to='app01.Items'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conditions',
            name='operator',
            field=models.ForeignKey(verbose_name='\u8fd0\u7b97\u7b26', blank=True, to='app01.Operators', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actions',
            name='condition_list',
            field=models.ManyToManyField(to='app01.Conditions'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actions',
            name='operation_list',
            field=models.ManyToManyField(to='app01.Operations'),
            preserve_default=True,
        ),
    ]

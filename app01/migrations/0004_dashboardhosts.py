# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20150831_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboardhosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('hosts', models.ManyToManyField(default=None, related_name='dashboard host', to='app01.Host')),
                ('ip', models.ManyToManyField(default=None, related_name='dashboard ip', to='app01.Host')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

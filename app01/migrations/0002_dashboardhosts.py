# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboardhosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u76d1\u6d4b\u4e3b\u673a')),
                ('hosts', models.ManyToManyField(default=None, related_name='monitor host', to='app01.Host')),
                ('ip', models.ManyToManyField(default=None, related_name='monitor ip', to='app01.Host')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

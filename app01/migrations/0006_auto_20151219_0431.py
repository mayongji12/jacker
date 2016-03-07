# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20150831_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardhosts',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='dashboardhosts',
            name='ip',
        ),
        migrations.AlterField(
            model_name='dashboardhosts',
            name='hosts',
            field=models.ManyToManyField(to='app01.Host'),
            preserve_default=True,
        ),
    ]

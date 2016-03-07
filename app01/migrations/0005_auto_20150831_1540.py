# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_dashboardhosts'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardhosts',
            name='groups',
            field=models.ManyToManyField(default=None, related_name='ip', to='app01.Group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dashboardhosts',
            name='hosts',
            field=models.ManyToManyField(default=None, related_name='hosts', to='app01.Host'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dashboardhosts',
            name='ip',
            field=models.ManyToManyField(default=None, to='app01.Host'),
            preserve_default=True,
        ),
    ]

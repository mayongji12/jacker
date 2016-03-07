# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_dashboardhosts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardhosts',
            name='hosts',
        ),
        migrations.RemoveField(
            model_name='dashboardhosts',
            name='ip',
        ),
        migrations.DeleteModel(
            name='Dashboardhosts',
        ),
    ]

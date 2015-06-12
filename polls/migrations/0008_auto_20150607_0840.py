# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20150607_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='members',
            field=models.ManyToManyField(default=None, related_name='selection', to='polls.Choiceship'),
        ),
    ]

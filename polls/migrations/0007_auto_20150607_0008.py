# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150512_2117'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='choiceship',
            name='student',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='members',
            field=models.ManyToManyField(related_name='selection', to='polls.Choiceship'),
        ),
    ]

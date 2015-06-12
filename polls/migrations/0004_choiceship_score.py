# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150512_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='choiceship',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]

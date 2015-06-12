# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150512_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='members',
            field=models.ManyToManyField(related_name='selection', to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_choiceship_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choiceship',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='choiceship',
            name='student',
        ),
        migrations.AddField(
            model_name='choice',
            name='members',
            field=models.ManyToManyField(related_name='groups', to='polls.Student'),
        ),
    ]

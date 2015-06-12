# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choiceship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.ForeignKey(to='polls.Choice')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='choice',
        ),
        migrations.AddField(
            model_name='choiceship',
            name='student',
            field=models.ForeignKey(to='polls.Student'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151112_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='likes',
            field=models.PositiveIntegerField(verbose_name='Likes', default=0),
        ),
    ]

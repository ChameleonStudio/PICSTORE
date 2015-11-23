# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_picture_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='sale',
            field=models.ForeignKey(null=True, blank=True, to='core.Sale', verbose_name='Sale'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='short_description',
            field=models.CharField(null=True, blank=True, max_length=511, verbose_name='Short description'),
        ),
    ]

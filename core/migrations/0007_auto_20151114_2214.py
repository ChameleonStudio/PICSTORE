# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151113_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='created',
            field=models.DateTimeField(default=timezone.now(), verbose_name='Created', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(null=True, blank=True, verbose_name='Description', max_length=511),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon_class',
            field=models.CharField(null=True, default='', blank=True, verbose_name='Icon class', max_length=100),
        ),
        migrations.AlterField(
            model_name='sale',
            name='description',
            field=models.CharField(null=True, blank=True, verbose_name='Description', max_length=511),
        ),
        migrations.AlterField(
            model_name='supercategory',
            name='description',
            field=models.CharField(null=True, blank=True, verbose_name='Description', max_length=511),
        ),
    ]

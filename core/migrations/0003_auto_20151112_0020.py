# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151110_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.CharField(max_length=511, verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='picture',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='pictures/thumbnail', verbose_name='Thumbnail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to='pictures/original', verbose_name='Picture'),
        ),
    ]

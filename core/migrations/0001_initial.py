# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.CharField(max_length=511, verbose_name='Description')),
                ('icon_class', models.CharField(default='', max_length=100, verbose_name='Icon class')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('sort_description', models.CharField(max_length=511, verbose_name='Sort description')),
                ('price', models.FloatField(default=0.0, verbose_name='Price')),
                ('photo', models.FileField(upload_to='products', verbose_name='Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('value', models.CharField(max_length=511, verbose_name='Value')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.CharField(max_length=511, verbose_name='Description')),
                ('icon_class', models.CharField(default='', max_length=100, verbose_name='Icon class')),
                ('category', models.ForeignKey(to='core.Category', verbose_name='Category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='properties',
            field=models.ManyToManyField(to='core.Property'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(to='core.Subcategory', verbose_name='Subcategory'),
        ),
    ]

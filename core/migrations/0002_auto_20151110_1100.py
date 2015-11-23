# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('short_description', models.CharField(verbose_name='Short description', max_length=511)),
                ('price', models.FloatField(verbose_name='Price', default=0.0)),
                ('picture', models.FileField(verbose_name='Picture', upload_to='pictures/original')),
                ('category', models.ForeignKey(verbose_name='Category', to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('value', models.FloatField(verbose_name='Value', default=1.0)),
                ('description', models.CharField(verbose_name='Description', max_length=511)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='properties',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
        migrations.AddField(
            model_name='picture',
            name='sale',
            field=models.ForeignKey(verbose_name='Sale', to='core.Sale'),
        ),
        migrations.AddField(
            model_name='picture',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
    ]

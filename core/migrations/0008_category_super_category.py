# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151114_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='super_category',
            field=models.ForeignKey(verbose_name='Super category', to='core.SuperCategory', null=True, blank=True),
        ),
    ]

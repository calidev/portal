# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen_destacada',
            field=models.ImageField(null=True, blank=True, upload_to='articulos/'),
        ),
    ]

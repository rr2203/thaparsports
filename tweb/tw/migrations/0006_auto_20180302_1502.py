# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-02 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tw', '0005_r_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='r_post',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='r_post',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='r_post',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='r_post',
            name='image4',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
# Generated by Django 2.2.3 on 2019-07-05 06:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190705_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comments',
            name='like_activated_author',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=255), default=list, size=None),
        ),
    ]

# Generated by Django 2.2.3 on 2019-08-16 00:18

import app_user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=app_user.models.file_path),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-04 04:47

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_photomodel_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photomodel',
            name='imageUrl',
            field=models.ImageField(null=True, upload_to=api.models.upload_to),
        ),
    ]
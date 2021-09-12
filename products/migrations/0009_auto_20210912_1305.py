# Generated by Django 3.2.7 on 2021-09-12 13:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_productmodel_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='date_added',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 9, 12, 13, 5, 10, 646011, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]

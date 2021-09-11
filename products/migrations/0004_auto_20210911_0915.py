# Generated by Django 3.2.7 on 2021-09-11 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210911_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]

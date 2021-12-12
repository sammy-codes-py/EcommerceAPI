# Generated by Django 3.2.7 on 2021-09-15 07:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0011_alter_productmodel_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('complete_order', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.IntegerField()),
                ('date_added', models.DateTimeField(verbose_name=datetime.datetime(2021, 9, 15, 7, 54, 59, 333158, tzinfo=utc))),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productmodel')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]
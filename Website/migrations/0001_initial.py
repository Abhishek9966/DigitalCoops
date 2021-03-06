# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 19:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[(b'Select category', b'-'), (b'Stationary', b'Stationary'), (b'Eatables', b'Eatables')], default=b'-', max_length=50)),
                ('quantity', models.IntegerField()),
                ('pic', models.FileField(blank=True, null=True, upload_to=b'static/images/')),
                ('specs', models.TextField()),
                ('unit_price', models.IntegerField()),
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItemSold',
            fields=[
                ('selling_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sell_date', models.DateField(null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Website.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('review_date', models.DateField(null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Website.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('transaction_id', models.IntegerField(primary_key=True, serialize=False)),
                ('transaction_date', models.DateField(null=True)),
                ('items_included', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('registration_number', models.IntegerField(default=0)),
                ('wallet_balance', models.FloatField(default=0)),
                ('course', models.CharField(choices=[(b'Btech', b'Btech'), (b'Mtech', b'Mtech'), (b'MCA', b'MCA')], default=b'-', max_length=50)),
                ('category', models.CharField(choices=[(b'Admin', b'Admin'), (b'Student', b'Student')], max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itemsold',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Website.Transactions'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart_present',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Website.UserProfile'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Website.Item'),
        ),
    ]

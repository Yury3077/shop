# Generated by Django 3.1.2 on 2021-03-01 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabric_shop', '0005_auto_20210301_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='article',
            field=models.CharField(default='', max_length=100),
        ),
    ]

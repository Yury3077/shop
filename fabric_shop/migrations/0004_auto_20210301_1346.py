# Generated by Django 3.1.2 on 2021-03-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabric_shop', '0003_auto_20210301_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='fabric_shop/static/fabric_shop/img/product'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-07-25 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_subcategory_time_in_minute'),
        ('notification', '0002_auto_20200725_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='categories',
            field=models.ManyToManyField(to='common.Category'),
        ),
    ]
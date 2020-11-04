# Generated by Django 3.0.7 on 2020-11-04 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_subcategory_time_in_minute'),
        ('notification', '0004_auto_20200811_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='categories',
        ),
        migrations.AddField(
            model_name='notification',
            name='subCategories',
            field=models.ManyToManyField(to='common.SubCategory'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-10-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20200724_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='district',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='District',
        ),
    ]

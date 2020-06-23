# Generated by Django 3.0.7 on 2020-06-21 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sub_level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.SubCategory'),
            preserve_default=False,
        ),
    ]

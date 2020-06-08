# Generated by Django 3.0.7 on 2020-06-06 20:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_auto_20200607_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='solution_number',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
            preserve_default=False,
        ),
    ]

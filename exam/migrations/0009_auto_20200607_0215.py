# Generated by Django 3.0.7 on 2020-06-06 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_auto_20200607_0151'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='question',
            constraint=models.UniqueConstraint(fields=('question_body', 'option1'), name='question constraint'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-09-20 23:34

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover_img', models.ImageField(upload_to='blog/cover')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ('-created_time',),
            },
        ),
    ]
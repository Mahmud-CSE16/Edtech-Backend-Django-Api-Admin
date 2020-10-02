# Generated by Django 3.0.7 on 2020-09-16 10:03

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goniter_itihash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoniterItihash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover_img', models.ImageField(upload_to='shop/cover')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'গনিতের ইতিহাস',
                'verbose_name_plural': 'গনিতের ইতিহাস',
                'ordering': ('title',),
            },
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
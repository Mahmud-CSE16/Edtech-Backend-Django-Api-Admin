# Generated by Django 3.0.7 on 2020-06-19 01:26

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.BooleanField(default=False)),
                ('question_body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('option1', ckeditor_uploader.fields.RichTextUploadingField()),
                ('option2', ckeditor_uploader.fields.RichTextUploadingField()),
                ('option3', ckeditor_uploader.fields.RichTextUploadingField()),
                ('option4', ckeditor_uploader.fields.RichTextUploadingField()),
                ('answer_number', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('solution', ckeditor_uploader.fields.RichTextUploadingField()),
                ('chapters', models.ManyToManyField(to='common.Chapter')),
                ('histories', models.ManyToManyField(blank=True, to='common.QuestionHistory')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Language')),
                ('subcategories', models.ManyToManyField(to='common.SubCategory')),
                ('types', models.ManyToManyField(to='common.QuestionType')),
            ],
        ),
    ]

# Generated by Django 4.0 on 2022-04-17 12:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0006_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bobstv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
                ('url', models.TextField()),
            ],
        ),
    ]

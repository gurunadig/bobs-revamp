# Generated by Django 4.0 on 2022-04-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0007_bobstv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, default='400-200.png', upload_to='')),
            ],
        ),
    ]
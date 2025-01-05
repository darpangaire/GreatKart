# Generated by Django 5.1.4 on 2025-01-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=100, unique=True)),
                ('slug', models.CharField(blank=True, max_length=100, unique=True)),
                ('images', models.ImageField(blank=True, upload_to='photos/categories')),
                ('description', models.TextField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
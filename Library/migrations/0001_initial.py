# Generated by Django 5.0.6 on 2024-06-11 10:36

import django.db.models.deletion
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
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('publication_year', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('book_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='Library.category')),
            ],
        ),
    ]

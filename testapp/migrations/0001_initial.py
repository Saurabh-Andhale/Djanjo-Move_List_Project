# Generated by Django 5.1 on 2024-10-08 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.DateField()),
                ('moviename', models.CharField(max_length=30)),
                ('hero', models.CharField(max_length=40)),
                ('heroine', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]

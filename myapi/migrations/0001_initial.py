# Generated by Django 3.2.4 on 2021-06-18 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('service', models.CharField(max_length=60)),
                ('hours', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=60)),
            ],
        ),
    ]

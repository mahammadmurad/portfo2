# Generated by Django 4.1.7 on 2023-10-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('prof', models.CharField(max_length=25)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='about')),
            ],
        ),
    ]

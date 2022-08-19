# Generated by Django 4.1 on 2022-08-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=20)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('phone', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
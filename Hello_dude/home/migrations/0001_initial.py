# Generated by Django 4.2.5 on 2023-11-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('text', models.CharField(max_length=120)),
                ('date', models.DateField(max_length=120)),
            ],
        ),
    ]

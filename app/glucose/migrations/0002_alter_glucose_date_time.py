# Generated by Django 3.2.13 on 2022-09-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glucose', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glucose',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

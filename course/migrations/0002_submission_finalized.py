# Generated by Django 3.0.3 on 2020-06-29 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='finalized',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 5.1.6 on 2025-04-07 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]

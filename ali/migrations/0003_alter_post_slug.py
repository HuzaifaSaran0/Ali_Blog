# Generated by Django 5.0.7 on 2024-08-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ali', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=150),
        ),
    ]

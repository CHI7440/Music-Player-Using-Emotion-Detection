# Generated by Django 5.0.1 on 2024-01-15 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='face_image',
            name='title',
        ),
    ]
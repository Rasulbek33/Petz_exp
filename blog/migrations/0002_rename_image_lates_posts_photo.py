# Generated by Django 5.0.1 on 2024-02-01 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lates_posts',
            old_name='image',
            new_name='photo',
        ),
    ]

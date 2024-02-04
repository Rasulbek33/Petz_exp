# Generated by Django 5.0.1 on 2024-02-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_lates_post_remove_blog_lates_photo_remove_blog_news_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lates_post',
        ),
        migrations.AddField(
            model_name='blog',
            name='lates_photo',
            field=models.ImageField(blank=True, help_text='photo', upload_to='blog/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='blog',
            name='news',
            field=models.CharField(blank=True, help_text='messege', max_length=30),
        ),
    ]

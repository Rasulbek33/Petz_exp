# Generated by Django 5.0.1 on 2024-02-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0002_alter_adoption_petz_name_delete_petz_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adoption_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petz_img', models.ImageField(help_text='petz_image', upload_to='petz_image/%Y/%m/%d')),
                ('petz_name', models.CharField(help_text='petz_name', max_length=30)),
                ('petz_news', models.CharField(help_text='petz_news', max_length=200)),
            ],
            options={
                'verbose_name': 'Adoption_name',
                'verbose_name_plural': 'Adoption_names',
            },
        ),
        migrations.RemoveField(
            model_name='adoption',
            name='petz_img',
        ),
        migrations.RemoveField(
            model_name='adoption',
            name='petz_name',
        ),
        migrations.RemoveField(
            model_name='adoption',
            name='petz_news',
        ),
        migrations.AlterField(
            model_name='adoption',
            name='about_sub_title',
            field=models.CharField(blank=True, help_text='about_sub_title', max_length=100),
        ),
        migrations.AlterField(
            model_name='adoption',
            name='about_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='about_title'),
        ),
        migrations.AlterField(
            model_name='adoption',
            name='photo',
            field=models.ImageField(blank=True, help_text='photo', upload_to='adoption/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='adoption',
            name='sub_title',
            field=models.TextField(blank=True, help_text='sub_title'),
        ),
        migrations.AlterField(
            model_name='adoption',
            name='title',
            field=models.CharField(blank=True, help_text='title', max_length=50),
        ),
    ]
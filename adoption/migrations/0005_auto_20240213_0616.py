# Generated by Django 3.2.12 on 2024-02-13 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0004_adoption_petz_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adoption',
            options={'verbose_name': 'Adoption', 'verbose_name_plural': 'Adoptions'},
        ),
        migrations.AddField(
            model_name='adoption',
            name='petz_img',
            field=models.ImageField(default=1, help_text='petz_image', upload_to='petz_image/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adoption',
            name='petz_news',
            field=models.CharField(default=1, help_text='petz_news', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adoption',
            name='petz_name',
            field=models.CharField(help_text='petz_name', max_length=30),
        ),
        migrations.DeleteModel(
            name='Adoption_name',
        ),
    ]

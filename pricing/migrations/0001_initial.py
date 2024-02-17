# Generated by Django 5.0.1 on 2024-02-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Our_plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(help_text='title', max_length=100)),
                ('sub_title', models.CharField(help_text='sub_title', max_length=255)),
                ('img', models.ImageField(help_text='image', upload_to='Our_plans/%Y/%m/%d')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('direction', models.CharField(help_text='direction', max_length=50)),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('species', models.CharField(help_text='species', max_length=50)),
            ],
            options={
                'verbose_name': 'Pricing',
                'verbose_name_plural': 'Pricings',
            },
        ),
    ]

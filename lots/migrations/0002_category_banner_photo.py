# Generated by Django 3.1.7 on 2021-03-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='banner_photo',
            field=models.ImageField(blank=True, null=True, upload_to='category_photo/', verbose_name='Баннерное изображение'),
        ),
    ]
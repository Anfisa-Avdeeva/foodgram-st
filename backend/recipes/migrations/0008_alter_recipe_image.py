# Generated by Django 3.2.16 on 2025-01-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_foodgramuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='recipe_images', verbose_name='Изображение'),
        ),
    ]

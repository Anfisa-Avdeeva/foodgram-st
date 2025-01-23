# Generated by Django 3.2.16 on 2025-01-23 22:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20250123_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Время приготовления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipes.Ingredient', verbose_name='Ингредиеты'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribing', to=settings.AUTH_USER_MODEL, verbose_name='Подписчик')),
            ],
            options={
                'unique_together': {('user', 'subscribing')},
            },
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-19 20:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_goods', '0003_goods_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=30, verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ManyToManyField(to='add_goods.category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=models.CharField(max_length=500, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(upload_to='photos', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='количество')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_goods.goods', verbose_name='товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'товар_в_корзине',
                'verbose_name_plural': 'товары_в_корзине',
            },
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-20 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_goods', '0004_alter_category_options_alter_goods_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'товар в корзине', 'verbose_name_plural': 'товары в корзине'},
        ),
    ]

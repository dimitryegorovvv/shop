# Generated by Django 5.0.6 on 2024-07-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_goods', '0005_alter_cartitem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='popularity',
            field=models.PositiveIntegerField(default=0, verbose_name='количество просмотров'),
        ),
    ]
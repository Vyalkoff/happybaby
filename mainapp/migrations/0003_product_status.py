# Generated by Django 4.0.6 on 2022-07-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_product_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[(None, 'Выберите если требуется'), ('sale', 'Распродажа'), ('new', 'Новинка')], max_length=6),
        ),
    ]

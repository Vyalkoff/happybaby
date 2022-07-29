# Generated by Django 4.0.6 on 2022-07-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='старая цена продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[(None, 'Выберите если требуется'), ('sale', 'Распродажа'), ('new', 'Новинка'), ('most', 'Популярно')], max_length=6),
        ),
    ]
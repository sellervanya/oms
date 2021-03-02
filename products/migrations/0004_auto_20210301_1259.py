# Generated by Django 3.1.4 on 2021-03-01 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210228_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(default='None.jpg', upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='measurement',
            field=models.CharField(choices=[('KG', 'кг.'), ('GR', 'гр.'), ('ML', 'мл.'), ('L', 'л.')], max_length=25),
        ),
        migrations.AlterField(
            model_name='drink',
            name='image',
            field=models.ImageField(default='None.jpg', upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='measurement',
            field=models.CharField(choices=[('KG', 'кг.'), ('GR', 'гр.'), ('ML', 'мл.'), ('L', 'л.')], max_length=25),
        ),
    ]
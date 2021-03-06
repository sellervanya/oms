# Generated by Django 3.1.4 on 2021-03-02 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210301_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True, verbose_name='Name')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('volume', models.IntegerField(verbose_name='Volume')),
                ('measurement', models.CharField(choices=[('KG', 'killogramm'), ('GR', 'gramm'), ('ML', 'mill'), ('L', 'liter')], max_length=25)),
                ('calories', models.IntegerField(verbose_name='Calories')),
                ('image', models.ImageField(default='None.jpg', upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True, verbose_name='Name')),
                ('alcohol', models.IntegerField(default=False, verbose_name='Alcohol percent')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'SubCategory',
                'verbose_name_plural': 'SubCategories',
            },
        ),
        migrations.RemoveField(
            model_name='drink',
            name='category',
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.DeleteModel(
            name='DishCategory',
        ),
        migrations.DeleteModel(
            name='Drink',
        ),
        migrations.DeleteModel(
            name='DrinkCategory',
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.subcategory'),
        ),
    ]

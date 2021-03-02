# Generated by Django 3.1.4 on 2021-02-27 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Категория блюда',
            },
        ),
        migrations.CreateModel(
            name='DrinkCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Категория напитка',
            },
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True, verbose_name='Имя')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('weight', models.IntegerField(verbose_name='Масса')),
                ('calories', models.IntegerField(verbose_name='Калории')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.drinkcategory')),
            ],
            options={
                'verbose_name': 'Напиток',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True, verbose_name='Имя')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('volume', models.IntegerField(verbose_name='Volume')),
                ('calories', models.IntegerField(verbose_name='Калории')),
                ('alcohol', models.BooleanField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.dishcategory')),
            ],
            options={
                'verbose_name': 'Dish',
            },
        ),
    ]

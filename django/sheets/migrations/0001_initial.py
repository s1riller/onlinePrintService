# Generated by Django 5.0.2 on 2024-03-15 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('symbol', models.CharField(max_length=20, verbose_name='Символ')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
            },
        ),
        migrations.CreateModel(
            name='UnitClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип единиц измерения',
                'verbose_name_plural': 'Типы единиц измерения',
            },
        ),
        migrations.CreateModel(
            name='ConversionFactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor', models.FloatField(verbose_name='Коэффициент конвертации')),
                ('from_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversion_factors_from', to='sheets.unit')),
                ('to_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversion_factors_to', to='sheets.unit')),
            ],
            options={
                'verbose_name': 'Коэффициент конвертации',
                'verbose_name_plural': 'Коэффициенты конвертации',
            },
        ),
        migrations.AddField(
            model_name='unit',
            name='classUnit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheets.unitclass'),
        ),
    ]

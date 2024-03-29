# Generated by Django 5.0.2 on 2024-03-15 10:48

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0003_unit_conversionfactor'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название материала')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за лист')),
            ],
            options={
                'verbose_name': 'Материал бумаги',
                'verbose_name_plural': 'Материалы бумаги',
            },
        ),
        migrations.AlterModelOptions(
            name='sheet',
            options={'verbose_name': 'Лист', 'verbose_name_plural': 'Листы'},
        ),
        migrations.AddField(
            model_name='sheet',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 3, 15, 18, 48, 18, 2341), verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sheet',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='sheet',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее изменение'),
        ),
        migrations.AddField(
            model_name='sheet',
            name='name',
            field=models.CharField(default=datetime.datetime(2024, 3, 15, 18, 48, 20, 563723), max_length=200, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sheet',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sheets.materialsheet'),
        ),
    ]

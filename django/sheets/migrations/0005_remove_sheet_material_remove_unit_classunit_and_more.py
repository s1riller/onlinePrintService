# Generated by Django 5.0.2 on 2024-03-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0004_materialsheet_alter_sheet_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sheet',
            name='material',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='classUnit',
        ),
        migrations.AlterModelOptions(
            name='sheet',
            options={'verbose_name': 'Формат бумаги', 'verbose_name_plural': 'Форматы бумаг'},
        ),
        migrations.AddField(
            model_name='sheet',
            name='length',
            field=models.FloatField(default=None, verbose_name='Длина мм'),
        ),
        migrations.AddField(
            model_name='sheet',
            name='width',
            field=models.FloatField(default=None, verbose_name='Ширина мм'),
        ),
        migrations.DeleteModel(
            name='ConversionFactor',
        ),
        migrations.DeleteModel(
            name='MaterialSheet',
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
        migrations.DeleteModel(
            name='UnitClass',
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-10 10:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_file_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='files', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

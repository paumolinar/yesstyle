# Generated by Django 5.1.4 on 2024-12-11 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='default brand', max_length=100),
            preserve_default=False,
        ),
    ]

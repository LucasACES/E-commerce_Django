# Generated by Django 3.1.2 on 2020-10-30 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_auto_20201030_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]

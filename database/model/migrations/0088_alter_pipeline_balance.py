# Generated by Django 3.2.23 on 2024-01-23 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0087_pipeline_strategy_combination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipeline',
            name='balance',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2 on 2021-04-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0045_auto_20210415_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='cummulative_quote_qty',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]

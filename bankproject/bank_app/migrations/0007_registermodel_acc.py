# Generated by Django 4.2.1 on 2023-07-05 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0006_registermodel_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='registermodel',
            name='acc',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.1 on 2023-07-25 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0015_wishlist_newsid'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='Uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

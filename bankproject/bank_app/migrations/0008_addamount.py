# Generated by Django 4.2.1 on 2023-07-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0007_registermodel_acc'),
    ]

    operations = [
        migrations.CreateModel(
            name='addamount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

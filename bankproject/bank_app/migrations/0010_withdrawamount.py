# Generated by Django 4.2.2 on 2023-07-11 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0009_mini'),
    ]

    operations = [
        migrations.CreateModel(
            name='withdrawamount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

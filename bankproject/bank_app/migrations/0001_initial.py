# Generated by Django 4.2.1 on 2023-06-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('photo', models.FileField(upload_to='bank_app/static')),
                ('pin', models.IntegerField()),
                ('repin', models.IntegerField()),
            ],
        ),
    ]

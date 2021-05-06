# Generated by Django 3.2 on 2021-04-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('describe', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
            ],
        ),
    ]
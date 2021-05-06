# Generated by Django 3.2 on 2021-04-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
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
# Generated by Django 4.1.3 on 2022-11-27 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25)),
                ('ldate', models.CharField(max_length=25)),
                ('addr', models.CharField(max_length=250)),
                ('num', models.IntegerField()),
                ('bill', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order_copy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25)),
                ('ldate', models.CharField(max_length=25)),
                ('addr', models.CharField(max_length=250)),
                ('num', models.IntegerField()),
                ('bill', models.IntegerField()),
            ],
        ),
    ]

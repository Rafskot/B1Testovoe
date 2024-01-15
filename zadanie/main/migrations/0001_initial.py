# Generated by Django 4.1.7 on 2024-01-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_1', models.FloatField()),
                ('value_2', models.FloatField()),
                ('value_3', models.FloatField()),
                ('value_4', models.FloatField()),
                ('value_5', models.FloatField()),
                ('value_6', models.FloatField()),
                ('value_7', models.FloatField()),
                ('class_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EndClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_1', models.CharField(max_length=255)),
                ('value_2', models.FloatField()),
                ('value_3', models.FloatField()),
                ('value_4', models.FloatField()),
                ('value_5', models.FloatField()),
                ('value_6', models.FloatField()),
                ('value_7', models.FloatField()),
                ('class_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EndTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_1', models.CharField(max_length=255)),
                ('value_2', models.FloatField()),
                ('value_3', models.FloatField()),
                ('value_4', models.FloatField()),
                ('value_5', models.FloatField()),
                ('value_6', models.FloatField()),
                ('value_7', models.FloatField()),
            ],
        ),
    ]
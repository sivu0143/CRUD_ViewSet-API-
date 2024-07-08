# Generated by Django 5.0.6 on 2024-07-08 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('Categoryname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('CategoryID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('prdouctname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
                ('Categoryname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productcategory')),
            ],
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-02 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]

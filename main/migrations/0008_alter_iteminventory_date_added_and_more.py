# Generated by Django 4.0.7 on 2022-11-27 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_staffinventory_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteminventory',
            name='date_added',
            field=models.DateField(default=datetime.date(2022, 11, 27)),
        ),
        migrations.AlterField(
            model_name='staffinventory',
            name='join_date',
            field=models.DateField(default=datetime.date(2022, 11, 27)),
        ),
    ]
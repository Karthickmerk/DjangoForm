# Generated by Django 2.1 on 2020-09-07 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_person_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
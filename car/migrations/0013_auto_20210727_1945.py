# Generated by Django 3.1.5 on 2021-07-27 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0012_auto_20210727_1944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['car_model']},
        ),
    ]

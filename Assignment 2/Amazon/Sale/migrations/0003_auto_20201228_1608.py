# Generated by Django 2.2 on 2020-12-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sale', '0002_auto_20201228_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='contact_person',
            field=models.CharField(max_length=255),
        ),
    ]

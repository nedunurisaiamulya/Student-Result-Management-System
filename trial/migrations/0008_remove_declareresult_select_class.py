# Generated by Django 2.2.7 on 2019-11-24 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0007_declareresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='declareresult',
            name='select_class',
        ),
    ]

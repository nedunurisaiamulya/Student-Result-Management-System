# Generated by Django 2.2.7 on 2019-11-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0018_auto_20191125_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
# Generated by Django 2.2.7 on 2019-11-24 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0016_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='subject',
            field=models.ForeignKey(default='BEEE', on_delete=django.db.models.deletion.CASCADE, to='trial.Subject'),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-25 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0022_remove_sem_select_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='sem',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='trial.Sem'),
        ),
    ]

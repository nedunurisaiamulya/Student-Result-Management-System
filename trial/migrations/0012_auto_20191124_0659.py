# Generated by Django 2.2.7 on 2019-11-24 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0011_auto_20191124_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declareresult',
            name='marks1',
            field=models.CharField(choices=[('O(Outstanding)', 'O(Outstanding)'), ('A+(Excellent)', 'A+(Excellent)'), ('A(Very Good)', 'A(Very Good)'), ('B+(Good)', 'B+(Good)'), ('B(Average)', 'B(Average)'), ('C(Pass)', 'C(Pass)'), ('F(Fail)', 'F(Fail)')], max_length=20),
        ),
    ]
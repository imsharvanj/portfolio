# Generated by Django 2.1.3 on 2019-11-09 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20191109_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]

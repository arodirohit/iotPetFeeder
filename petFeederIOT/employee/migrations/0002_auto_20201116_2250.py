# Generated by Django 3.0.3 on 2020-11-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodlevelmonitor',
            name='RecordedTime',
            field=models.CharField(max_length=15),
        ),
    ]
# Generated by Django 3.0.3 on 2020-11-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='BowlWeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BowlWeightID', models.CharField(max_length=20)),
                ('BowlWeightDate', models.CharField(max_length=20)),
                ('BowlWeightAfter', models.FloatField()),
                ('BowlWeightBefore', models.FloatField()),
            ],
            options={
                'db_table': 'bowlWeight',
            },
        ),
        migrations.CreateModel(
            name='FoodContainerWeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContainerDate', models.CharField(max_length=20)),
                ('WeightAfterRelease', models.FloatField()),
                ('WeightBeforeRelease', models.FloatField()),
            ],
            options={
                'db_table': 'containerWeight',
            },
        ),
        migrations.CreateModel(
            name='FoodLevelMonitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RecordedTime', models.TimeField()),
                ('FoodLevelStatus', models.BooleanField()),
            ],
            options={
                'db_table': 'FoodLevel',
            },
        ),
        migrations.CreateModel(
            name='VoiceCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CmdID', models.CharField(max_length=20)),
                ('CmdDate', models.CharField(max_length=100)),
                ('CmdTime', models.TimeField()),
                ('CmdStatus', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'command',
            },
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
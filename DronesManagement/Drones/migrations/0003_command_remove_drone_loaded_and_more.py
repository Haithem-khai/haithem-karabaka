# Generated by Django 4.0 on 2021-12-29 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Drones', '0002_alter_drone_loadedmedication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='drone',
            name='loaded',
        ),
        migrations.RemoveField(
            model_name='drone',
            name='loadedMedication',
        ),
        migrations.AlterField(
            model_name='drone',
            name='model',
            field=models.CharField(choices=[('Lightweight', 'Lightweight'), ('Middleweight', 'Middleweight'), ('Cruiserweight', 'Cruiserweight'), ('Heavyweight', 'Heavyweight')], max_length=50),
        ),
        migrations.AlterField(
            model_name='drone',
            name='state',
            field=models.CharField(choices=[('IDLE', 'IDLE'), ('LOADING', 'LOADING'), ('LOADED', 'LOADED'), ('DELIVERING', 'DELIVERING'), ('DELIVERED', 'DELIVERED'), ('RETURNING', 'RETURNING')], max_length=50),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionId', models.CharField(max_length=150)),
                ('achieved', models.BooleanField(default=False)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Drones.command')),
            ],
        ),
        migrations.AddField(
            model_name='command',
            name='drone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Drones.drone'),
        ),
        migrations.AddField(
            model_name='command',
            name='medication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Drones.medication'),
        ),
    ]

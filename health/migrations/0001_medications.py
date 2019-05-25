# Generated by Django 2.2 on 2019-05-25 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0007_temperature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('dose_type', models.CharField(help_text='Pill, shot, ml, mg, etc.', max_length=255, verbose_name='Dose type')),
            ],
            options={
                'verbose_name': 'Medication',
                'verbose_name_plural': 'Medications',
                'ordering': ['name'],
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='MedicationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dose', models.PositiveIntegerField(verbose_name='Dose')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_date', models.DateField(null=True, verbose_name='End date')),
                ('end_time', models.TimeField(null=True, verbose_name='End time')),
                ('recurring', models.BooleanField(default=False, verbose_name='Recurring')),
                ('recurring_type', models.CharField(blank=True, choices=[('hourly', 'Hourly'), ('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=255, verbose_name='Frequency')),
                ('separation_count', models.PositiveIntegerField(blank=True, null=True, verbose_name='Separation')),
                ('max_occurrences', models.PositiveIntegerField(blank=True, null=True, verbose_name='Max occurrences')),
                ('dow', models.PositiveIntegerField(blank=True, null=True, verbose_name='Day of week')),
                ('hod', models.PositiveIntegerField(blank=True, null=True, verbose_name='Hour of day')),
                ('wom', models.PositiveIntegerField(blank=True, null=True, verbose_name='Week of month')),
                ('dom', models.PositiveIntegerField(blank=True, null=True, verbose_name='Day of month')),
                ('moy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Month of year')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication_event', to='core.Child', verbose_name='Child')),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication_event', to='health.Medication', verbose_name='Medication')),
            ],
            options={
                'verbose_name': 'Medication event',
                'verbose_name_plural': 'Medication events',
                'ordering': ['-start_date', '-start_time'],
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='MedicationAdministration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administered', models.BooleanField(default=True, verbose_name='Administered')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication_administration', to='core.Child', verbose_name='Child')),
                ('medication_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication_administration', to='health.MedicationEvent', verbose_name='Medication event')),
            ],
            options={
                'verbose_name': 'Medication administration',
                'verbose_name_plural': 'Medication administrations',
                'ordering': ['-date', '-time'],
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
    ]

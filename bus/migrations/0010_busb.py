# Generated by Django 4.1.1 on 2022-12-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0009_alter_ticket_booking_booking_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('dest', models.CharField(max_length=30)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('rem', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
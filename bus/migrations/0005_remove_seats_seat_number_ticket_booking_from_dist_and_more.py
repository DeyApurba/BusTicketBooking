# Generated by Django 4.1.1 on 2022-12-11 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0001_initial'),
        ('bus', '0004_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seats',
            name='seat_number',
        ),
        migrations.AddField(
            model_name='ticket_booking',
            name='from_dist',
            field=models.CharField(default='Null', max_length=20),
        ),
        migrations.AlterField(
            model_name='bus',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='passenger.passenger'),
        ),
    ]

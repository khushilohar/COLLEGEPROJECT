# Generated by Django 4.2.2 on 2023-12-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('AC', 'AC'), ('NON-AC', 'NON-AC'), ('DELUXE', 'DELUXE'), ('KING', 'KING'), ('QUEEN', 'QUEEN')], max_length=20),
        ),
    ]

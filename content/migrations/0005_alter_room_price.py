# Generated by Django 4.1.5 on 2023-01-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_room_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
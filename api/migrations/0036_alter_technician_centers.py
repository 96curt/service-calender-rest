# Generated by Django 4.1 on 2022-12-28 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_alter_manager_region_alter_schedule_technicians'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technician',
            name='centers',
            field=models.ManyToManyField(related_name='technicians', to='api.servicecenter'),
        ),
    ]

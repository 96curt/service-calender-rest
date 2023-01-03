# Generated by Django 4.1 on 2022-12-29 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_zipcode_region_alter_city_region_remove_zipcode_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zipcode',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zipCodes_set', to='api.region'),
        ),
    ]

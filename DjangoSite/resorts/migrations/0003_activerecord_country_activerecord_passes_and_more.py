# Generated by Django 4.1.4 on 2022-12-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resorts', '0002_rename_snow_bae_depth_activerecord_snow_base_depth'),
    ]

    operations = [
        migrations.AddField(
            model_name='activerecord',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='activerecord',
            name='passes',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='activerecord',
            name='region',
            field=models.CharField(default='', max_length=50),
        ),
    ]
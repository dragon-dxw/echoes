# Generated by Django 3.1 on 2020-08-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_vision_soul_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vision',
            name='dose_origin',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]

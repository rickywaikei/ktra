# Generated by Django 4.2.17 on 2025-01-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_service_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='instructor',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='service',
            name='location',
            field=models.CharField(default='Kwun Tong Residence Association', max_length=100),
            preserve_default=False,
        ),
    ]
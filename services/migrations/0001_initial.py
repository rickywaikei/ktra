# Generated by Django 4.2 on 2025-01-06 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('service_type', models.CharField(choices=[('Elderly', '長者'), ('Youth', '青年'), ('Family', '家庭及兒童'), ('Class', '興趣班'), ('Communities', '社區共融'), ('other', '其他')], max_length=50)),
                ('description', models.TextField(blank=True)),
                ('service_date', models.DateField(default=django.utils.timezone.now)),
                ('service_start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('service_end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('fee', models.IntegerField(default=0)),
                ('quota', models.IntegerField(blank=True)),
                ('is_publish', models.BooleanField(default=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='services.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

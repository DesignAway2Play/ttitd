# Generated by Django 2.2 on 2019-06-17 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('bio', models.TextField(max_length=250)),
                ('social_link', models.CharField(max_length=100)),
                ('exp', models.IntegerField(default=0)),
                ('ghost_key', models.BooleanField(default=False)),
                ('user_key', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

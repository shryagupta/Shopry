# Generated by Django 2.2.11 on 2020-03-20 18:23

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
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Others', 'O')], default='Female', max_length=8)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-07 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='')),
                ('password', models.CharField(max_length=50, verbose_name='')),
                ('role', models.CharField(max_length=50, verbose_name='')),
                ('status', models.CharField(max_length=50, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='employee_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50, verbose_name='')),
                ('emp_email', models.CharField(max_length=50, verbose_name='')),
                ('emp_position', models.CharField(max_length=50, verbose_name='')),
                ('emp_contactno', models.BigIntegerField(verbose_name='')),
                ('emp_date', models.DateTimeField(verbose_name='')),
                ('auth_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_auth', to='superadmin.user_auth')),
            ],
        ),
    ]

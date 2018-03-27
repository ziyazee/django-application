# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-27 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, choices=[('f', 'female'), ('m', 'male')], max_length=1)),
                ('submission', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Myjob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='myinfo',
            name='myjob',
            field=models.ManyToManyField(blank=True, to='letsdoit.Myjob'),
        ),
    ]
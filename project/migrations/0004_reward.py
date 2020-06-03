# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 18:15
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Write the title for this kind of Reward', max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField(help_text='Write the detail for this kind of Reward', null=True)),
                ('reward_amout', models.DecimalField(decimal_places=2, help_text='How much does the donor have to pay to get this reward?', max_digits=15)),
                ('is_digital_product', models.BooleanField(default=False, help_text='Is it digital product like pdf/ebook that does not need shipping?')),
                ('shipping_date', models.DateField(help_text='When will the reward be ready?')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_for_reward', to='project.Project')),
            ],
        ),
    ]
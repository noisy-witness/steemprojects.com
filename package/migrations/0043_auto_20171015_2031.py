# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-15 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_accounttype_social_auth_provider_name'),
        ('package', '0042_auto_20171013_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammembership',
            name='confirmed_by_project_owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approvers', to='profiles.Account'),
        ),
        migrations.AddField(
            model_name='teammembership',
            name='project_owner',
            field=models.BooleanField(default=False, verbose_name='Project owner'),
        ),
        migrations.RenameField(
            model_name='teammembership',
            old_name="role_confirmed",
            new_name="role_confirmed_by_account"
        )
    ]

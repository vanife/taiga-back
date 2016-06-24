# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-24 15:32
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taiga.projects.notifications.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userstories', '0012_auto_20160614_1201'),
        ('projects', '0049_auto_20160624_1532'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=[], null=True, size=None, verbose_name='tags')),
                ('version', models.IntegerField(default=1, verbose_name='version')),
                ('is_blocked', models.BooleanField(default=False, verbose_name='is blocked')),
                ('blocked_note', models.TextField(blank=True, default='', verbose_name='blocked note')),
                ('ref', models.BigIntegerField(blank=True, db_index=True, default=None, null=True, verbose_name='ref')),
                ('is_closed', models.BooleanField(default=False)),
                ('epics_order', models.IntegerField(default=10000, verbose_name='epics order')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date')),
                ('finish_date', models.DateTimeField(blank=True, null=True, verbose_name='finish date')),
                ('subject', models.TextField(verbose_name='subject')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('client_requirement', models.BooleanField(default=False, verbose_name='is client requirement')),
                ('team_requirement', models.BooleanField(default=False, verbose_name='is team requirement')),
                ('assigned_to', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='epics_assigned_to_me', to=settings.AUTH_USER_MODEL, verbose_name='assigned to')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_epics', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epics', to='projects.Project', verbose_name='project')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='epics', to='projects.EpicStatus', verbose_name='status')),
                ('user_stories', models.ManyToManyField(related_name='epics', to='userstories.UserStory', verbose_name='user stories')),
            ],
            options={
                'verbose_name_plural': 'epics',
                'verbose_name': 'epic',
                'ordering': ['project', 'ref'],
            },
            bases=(taiga.projects.notifications.mixins.WatchedModelMixin, models.Model),
        ),
    ]

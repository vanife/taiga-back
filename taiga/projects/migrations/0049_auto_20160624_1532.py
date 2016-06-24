# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-24 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0048_auto_20160615_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='EpicStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='slug')),
                ('order', models.IntegerField(default=10, verbose_name='order')),
                ('is_closed', models.BooleanField(default=False, verbose_name='is closed')),
                ('color', models.CharField(default='#999999', max_length=20, verbose_name='color')),
            ],
            options={
                'verbose_name_plural': 'epic statuses',
                'ordering': ['project', 'order', 'name'],
                'verbose_name': 'epic status',
            },
        ),
        migrations.AlterModelOptions(
            name='issuestatus',
            options={'ordering': ['project', 'order', 'name'], 'verbose_name': 'issue status', 'verbose_name_plural': 'issue statuses'},
        ),
        migrations.AlterModelOptions(
            name='issuetype',
            options={'ordering': ['project', 'order', 'name'], 'verbose_name': 'issue type', 'verbose_name_plural': 'issue types'},
        ),
        migrations.AlterModelOptions(
            name='membership',
            options={'ordering': ['project', 'user__full_name', 'user__username', 'user__email', 'email'], 'verbose_name': 'membership', 'verbose_name_plural': 'memberships'},
        ),
        migrations.AlterModelOptions(
            name='points',
            options={'ordering': ['project', 'order', 'name'], 'verbose_name': 'points', 'verbose_name_plural': 'points'},
        ),
        migrations.AlterModelOptions(
            name='priority',
            options={'ordering': ['project', 'order', 'name'], 'verbose_name': 'priority', 'verbose_name_plural': 'priorities'},
        ),
        migrations.AlterModelOptions(
            name='severity',
            options={'ordering': ['project', 'order', 'name'], 'verbose_name': 'severity', 'verbose_name_plural': 'severities'},
        ),
        migrations.AlterModelOptions(
            name='taskstatus',
            options={'ordering': ['project', 'order', 'name'], 'verbose_name': 'task status', 'verbose_name_plural': 'task statuses'},
        ),
        migrations.AlterModelOptions(
            name='userstorystatus',
            options={'ordering': ['project', 'order', 'name'], 'verbose_name': 'user story status', 'verbose_name_plural': 'user story statuses'},
        ),
        migrations.AddField(
            model_name='project',
            name='is_epics_activated',
            field=models.BooleanField(default=True, verbose_name='active epics panel'),
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='epic_statuses',
            field=django_pgjson.fields.JsonField(blank=True, null=True, verbose_name='epic statuses'),
        ),
        migrations.AddField(
            model_name='epicstatus',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epic_statuses', to='projects.Project', verbose_name='project'),
        ),
        migrations.AddField(
            model_name='project',
            name='default_epic_status',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='projects.EpicStatus', verbose_name='default epic status'),
        ),
        migrations.AlterUniqueTogether(
            name='epicstatus',
            unique_together=set([('project', 'name'), ('project', 'slug')]),
        ),
    ]
# Generated by Django 1.11.11 on 2018-03-27 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0024_metafields'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppStatusFormStaging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, default=None, max_length=255)),
                ('app_id', models.CharField(db_index=True, max_length=255, null=True)),
                ('user_id', models.CharField(db_index=True, max_length=255, null=True)),
                ('last_submission', models.DateTimeField(db_index=True)),
                ('submission_build_version', models.CharField(db_index=True, max_length=255, null=True)),
                ('commcare_version', models.CharField(db_index=True, max_length=255, null=True)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='warehouse.Batch')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AppStatusSynclogStaging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_sync', models.DateTimeField(db_index=True, null=True)),
                ('domain', models.CharField(db_index=True, max_length=255, null=True)),
                ('user_id', models.CharField(db_index=True, max_length=255, null=True)),
                ('sync_build_version', models.CharField(db_index=True, max_length=255, null=True)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='warehouse.Batch')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='applicationstatusfact',
            name='app_id',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='applicationstatusfact',
            name='domain',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='applicationstatusfact',
            name='user_id',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicationstatusfact',
            name='last_form_app_build_version',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicationstatusfact',
            name='last_form_app_commcare_version',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicationstatusfact',
            name='last_sync_log_app_build_version',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='applicationstatusfact',
            name='last_form_app_source',
        ),
        migrations.RemoveField(
            model_name='applicationstatusfact',
            name='last_sync_log_app_commcare_version',
        ),
        migrations.RemoveField(
            model_name='applicationstatusfact',
            name='last_sync_log_app_source',
        ),
        migrations.RemoveField(
            model_name='applicationstatusfact',
            name='user_dim',
        ),
        migrations.AlterUniqueTogether(
            name='applicationstatusfact',
            unique_together=set([('app_id', 'user_id')]),
        ),
    ]

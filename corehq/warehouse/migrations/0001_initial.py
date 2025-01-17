# Generated by Django 1.10.7 on 2017-05-16 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainDim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255)),
                ('dim_last_modified', models.DateTimeField(auto_now=True)),
                ('dim_created_on', models.DateTimeField(auto_now_add=True)),
                ('domain_id', models.CharField(max_length=255)),
                ('default_timezone', models.CharField(max_length=255)),
                ('hr_name', models.CharField(max_length=255)),
                ('creating_user_id', models.CharField(max_length=255)),
                ('project_type', models.CharField(max_length=255)),
                ('is_active', models.BooleanField()),
                ('case_sharing', models.BooleanField()),
                ('commtrack_enabled', models.BooleanField()),
                ('is_test', models.BooleanField()),
                ('location_restriction_for_users', models.BooleanField()),
                ('use_sql_backend', models.BooleanField()),
                ('first_domain_for_user', models.BooleanField()),
                ('domain_last_modified', models.DateTimeField()),
                ('domain_created_on', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupDim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255)),
                ('dim_last_modified', models.DateTimeField(auto_now=True)),
                ('dim_created_on', models.DateTimeField(auto_now_add=True)),
                ('group_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('case_sharing', models.BooleanField()),
                ('reporting', models.BooleanField()),
                ('group_last_modified', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationDim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255)),
                ('dim_last_modified', models.DateTimeField(auto_now=True)),
                ('dim_created_on', models.DateTimeField(auto_now_add=True)),
                ('location_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('site_code', models.CharField(max_length=255)),
                ('external_id', models.CharField(max_length=255)),
                ('supply_point_id', models.CharField(max_length=255, null=True)),
                ('location_type_id', models.CharField(max_length=255)),
                ('location_type_name', models.CharField(max_length=255)),
                ('location_type_code', models.CharField(max_length=255)),
                ('is_archived', models.BooleanField()),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('location_last_modified', models.DateTimeField()),
                ('location_created_on', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=255)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('last_batch_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserDim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255)),
                ('dim_last_modified', models.DateTimeField(auto_now=True)),
                ('dim_created_on', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=255)),
                ('user_type', models.CharField(max_length=100)),
                ('is_active', models.BooleanField()),
                ('is_staff', models.BooleanField()),
                ('is_superuser', models.BooleanField()),
                ('last_login', models.DateTimeField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroupDim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255)),
                ('dim_last_modified', models.DateTimeField(auto_now=True)),
                ('dim_created_on', models.DateTimeField(auto_now_add=True)),
                ('group_dim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.GroupDim')),
                ('user_dim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.UserDim')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserLocationDim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255)),
                ('dim_last_modified', models.DateTimeField(auto_now=True)),
                ('dim_created_on', models.DateTimeField(auto_now_add=True)),
                ('location_dim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.LocationDim')),
                ('user_dim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.UserDim')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

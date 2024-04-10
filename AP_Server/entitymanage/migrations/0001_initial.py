# Generated by Django 4.0 on 2024-04-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntityInfo',
            fields=[
                ('entity_index', models.AutoField(primary_key=True, serialize=False, verbose_name='entity_name')),
                ('entity_pid', models.CharField(max_length=32, verbose_name='entity pid')),
                ('software_id', models.CharField(max_length=32, verbose_name='software_id')),
                ('user_id', models.CharField(max_length=32, verbose_name='user id')),
                ('entity_parcialkey', models.TextField(null=True, verbose_name='entity parcial key')),
                ('entity_porecessid', models.CharField(max_length=20, null=True, verbose_name='entity process id')),
                ('entity_port', models.IntegerField(null=True, verbose_name='entity port')),
                ('entity_ip', models.CharField(max_length=15, verbose_name='entity ip')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('is_alive', models.BooleanField(default=False, verbose_name='entity alive')),
            ],
        ),
    ]

# Generated by Django 4.0 on 2024-04-14 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entitymanage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicParamtersTable',
            fields=[
                ('kgc_id', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='kgc_id')),
                ('acc_publickey', models.TextField(verbose_name='acc_publickey')),
                ('acc_cur', models.TextField(verbose_name='acc_cur')),
                ('kgc_q', models.TextField(verbose_name='kgc_q')),
                ('kgc_Ppub', models.TextField(verbose_name='kgc_PpublicKey')),
            ],
        ),
        migrations.AddField(
            model_name='entityinfo',
            name='software_hash',
            field=models.CharField(default=0, max_length=32, verbose_name='software hash'),
            preserve_default=False,
        ),
    ]

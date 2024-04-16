# Generated by Django 4.0 on 2024-04-12 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entitymanage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KGCParamterTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kgc_id', models.CharField(max_length=32, verbose_name='kgc id')),
                ('kgc_s', models.TextField(verbose_name='kgc s')),
                ('kgc_Ppub', models.TextField(verbose_name='kgc Ppub')),
                ('kgc_q', models.TextField(verbose_name='kgc q')),
                ('kgc_acc_G', models.TextField(verbose_name='kgc acc G')),
                ('kgc_acc_publickey', models.TextField(verbose_name='kgc acc public key')),
                ('kgc_acc_cur', models.TextField(verbose_name='kgc acc cur')),
                ('kgc_acc_serectkey0', models.TextField(verbose_name='kgc acc serect key 0')),
                ('kgc_acc_serectkey1', models.TextField(verbose_name='kgc acc serect key 1')),
            ],
        ),
    ]

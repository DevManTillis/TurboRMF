# Generated by Django 2.0 on 2018-01-17 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_auto_20180105_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuln',
            name='v_con',
            field=models.CharField(default='NONE', max_length=1500),
        ),
        migrations.AlterField(
            model_name='vuln',
            name='v_dis',
            field=models.CharField(default='NONE', max_length=1500),
        ),
        migrations.AlterField(
            model_name='vuln',
            name='v_fix',
            field=models.CharField(default='NONE', max_length=1500),
        ),
    ]

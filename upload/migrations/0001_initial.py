# Generated by Django 2.0 on 2017-12-31 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklist_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('checklist_name', models.CharField(max_length=200)),
                ('checklist_owner', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(default='NONE', max_length=200)),
                ('document_owner', models.CharField(default='NONE', max_length=200)),
                ('document_data', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vuln',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_ids', models.CharField(max_length=200)),
                ('vuln_text', models.CharField(max_length=200)),
                ('v_sev', models.CharField(max_length=200)),
                ('v_dis', models.CharField(max_length=200)),
                ('v_con', models.CharField(max_length=200)),
                ('v_fix', models.CharField(max_length=200)),
                ('v_ref', models.CharField(max_length=200)),
                ('v_sta', models.CharField(max_length=200)),
                ('v_com', models.CharField(max_length=200)),
                ('v_det', models.CharField(max_length=200)),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.Checklist')),
            ],
        ),
    ]
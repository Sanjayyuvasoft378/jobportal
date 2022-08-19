# Generated by Django 3.2.15 on 2022-08-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('phoneNo', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'CandidateInfo',
            },
        ),
    ]

# Generated by Django 3.0.2 on 2020-05-01 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_assignments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ttitle', models.CharField(max_length=100)),
                ('TFile', models.FileField(upload_to='Assignment')),
            ],
        ),
    ]

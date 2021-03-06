# Generated by Django 3.2.12 on 2022-03-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='interviewee',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='interviewer',
        ),
        migrations.AddField(
            model_name='schedule',
            name='intervieweeEmail',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='schedule',
            name='intervieweeName',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='schedule',
            name='interviewerEmail',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='schedule',
            name='interviewerName',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

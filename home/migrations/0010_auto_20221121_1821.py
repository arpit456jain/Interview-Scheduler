# Generated by Django 3.2.12 on 2022-11-21 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_id_candidates_candidate_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='candidates',
        ),
        migrations.AddField(
            model_name='candidates',
            name='interview_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.schedule'),
            preserve_default=False,
        ),
    ]

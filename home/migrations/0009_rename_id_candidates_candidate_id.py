# Generated by Django 3.2.6 on 2022-11-21 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20221121_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidates',
            old_name='id',
            new_name='candidate_id',
        ),
    ]

# Generated by Django 3.2.12 on 2022-11-21 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_auto_20221121_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidates',
            name='candidate_email',
        ),
        migrations.AlterField(
            model_name='candidates',
            name='candidate_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

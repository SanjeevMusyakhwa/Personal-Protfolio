# Generated by Django 5.1.2 on 2024-10-25 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0002_remove_skilldata_skills_skilldata_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skilldata',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='data', to='skill.skill'),
        ),
    ]
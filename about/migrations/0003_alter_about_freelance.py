# Generated by Django 5.1.2 on 2024-10-25 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_about_freelance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='Freelance',
            field=models.BooleanField(choices=[('active', 'Active'), ('inactive', 'InActive')], default='Inactive', max_length=20, verbose_name='Freelancing'),
        ),
    ]

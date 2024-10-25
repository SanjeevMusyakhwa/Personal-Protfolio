# Generated by Django 5.1.2 on 2024-10-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('typed', models.CharField(help_text='Type Like This -> Designer, Developer, Freelancer, Photographer', max_length=255, verbose_name='typed')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('twitter', models.URLField(verbose_name='Twitter')),
                ('linkedIn', models.URLField(verbose_name='LinkedIn')),
                ('github', models.URLField(verbose_name='Github')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('image', models.ImageField(upload_to='profile/', verbose_name='About Profile')),
            ],
        ),
    ]
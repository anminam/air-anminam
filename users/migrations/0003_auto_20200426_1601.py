# Generated by Django 3.0.5 on 2020-04-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200426_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('kr', 'Korean'), ('en', 'English')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male'), ('other', 'Other')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('kr', 'Korean'), ('en', 'English')], max_length=2, null=True),
        ),
    ]
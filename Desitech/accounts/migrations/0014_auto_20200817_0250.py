# Generated by Django 3.0.9 on 2020-08-16 23:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200809_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_profile',
            name='building_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company_profile',
            name='mobile_number',
            field=models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='company_profile',
            name='phone_number',
            field=models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='company_profile',
            name='street',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='company_profile',
            name='zip_code',
            field=models.CharField(max_length=12, null=True, verbose_name='ZIP / Postal code'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'company'), (2, 'job_seeker')]),
        ),
    ]

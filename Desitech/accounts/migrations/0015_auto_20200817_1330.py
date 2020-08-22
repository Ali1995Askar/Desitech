# Generated by Django 3.0.9 on 2020-08-17 10:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200817_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='CV',
            field=models.FileField(null=True, upload_to='CV/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='country_of_residence',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='cover_letter',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='personal_photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='street',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='surname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='zip_code',
            field=models.CharField(max_length=12, null=True, verbose_name='ZIP / Postal code'),
        ),
    ]

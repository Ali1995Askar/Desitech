# Generated by Django 3.0.9 on 2020-08-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200808_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='text',
            new_name='abstract',
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.5 on 2021-03-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_userprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

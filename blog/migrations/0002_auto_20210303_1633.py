# Generated by Django 2.1.5 on 2021-03-03 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogarticles',
            options={'ordering': ('-publish',), 'verbose_name_plural': 'Blog Articles'},
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]

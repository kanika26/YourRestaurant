# Generated by Django 2.2.7 on 2019-12-03 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_onlinefoodorderform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='onlinefoodorderform',
            new_name='onlineorderform',
        ),
        migrations.RenameField(
            model_name='onlineorderform',
            old_name='phonenumber',
            new_name='phoneno',
        ),
    ]

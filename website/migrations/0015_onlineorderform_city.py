# Generated by Django 2.2.7 on 2019-12-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20191203_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlineorderform',
            name='city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.5 on 2019-11-21 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20191120_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartobject',
            name='userid',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

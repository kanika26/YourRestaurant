# Generated by Django 2.1.5 on 2019-11-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20191118_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

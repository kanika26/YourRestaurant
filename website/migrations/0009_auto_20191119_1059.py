# Generated by Django 2.1.5 on 2019-11-19 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_cartobject_producttitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartobject',
            name='price',
            field=models.CharField(max_length=200),
        ),
    ]
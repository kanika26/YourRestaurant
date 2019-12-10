# Generated by Django 2.1.5 on 2019-11-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20191118_0633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('img1', models.ImageField(upload_to='media')),
                ('img2', models.ImageField(upload_to='media')),
                ('price', models.CharField(max_length=300)),
                ('Pcategory', models.CharField(max_length=300)),
                ('Scategory', models.CharField(max_length=300)),
                ('available', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('userid', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'CartTable',
            },
        ),
    ]

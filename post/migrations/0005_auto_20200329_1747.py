# Generated by Django 3.0.4 on 2020-03-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200327_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]

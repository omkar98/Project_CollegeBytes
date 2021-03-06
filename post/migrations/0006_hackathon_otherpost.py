# Generated by Django 3.0.4 on 2020-04-01 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20200329_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Not specified', max_length=100)),
                ('team_size', models.IntegerField(default=1)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('desc', models.TextField(default='N.A')),
                ('eligibility', models.TextField(default='N.A', null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('views', models.IntegerField(default=1)),
                ('organizer', models.CharField(default='N.A.', max_length=100)),
                ('website', models.TextField(max_length=200, null=True)),
                ('author', models.CharField(default='N.A.', max_length=100)),
                ('author_email', models.CharField(default='N.A.', max_length=100)),
                ('organizer_logo', models.TextField(null=True)),
                ('status', models.IntegerField(choices=[(1, 'APPROVE'), (2, 'KEEP AS DRAFT'), (3, 'REJECT')], default=2)),
                ('last_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OtherPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Not specified', max_length=100)),
                ('desc', models.TextField(default='N.A')),
                ('eligibility', models.TextField(default='N.A', null=True)),
                ('date_posted', models.DateField(null=True)),
                ('views', models.IntegerField(default=1)),
                ('organizer', models.CharField(default='N.A.', max_length=100)),
                ('website', models.TextField(max_length=200, null=True)),
                ('author', models.CharField(default='N.A.', max_length=100)),
                ('author_email', models.CharField(default='N.A.', max_length=100)),
                ('organizer_logo', models.TextField(null=True)),
                ('status', models.IntegerField(choices=[(1, 'APPROVE'), (2, 'KEEP AS DRAFT'), (3, 'REJECT')], default=2)),
            ],
        ),
    ]

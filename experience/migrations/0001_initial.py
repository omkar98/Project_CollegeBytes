# Generated by Django 3.0.4 on 2020-04-04 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(default='Admin', max_length=100)),
                ('author_email', models.CharField(max_length=100)),
                ('author_about', models.TextField()),
                ('result_field', models.IntegerField(choices=[(1, 'Accepted'), (2, 'Rejected'), (3, 'Not Declared Yet'), (4, 'None of these')], null=True)),
                ('experience_result_more', models.CharField(max_length=100, null=True)),
                ('experience_type_field', models.IntegerField(choices=[(1, 'JOB INTERVIEW EXPERIENCE'), (2, 'INTERNSHIP EXPERIENCE'), (3, 'HACKATHON EXPERIENCE'), (4, 'OTHER EXPERIENCE')], default=4)),
                ('organization_name', models.CharField(max_length=100, null=True)),
                ('organization_role', models.CharField(max_length=100, null=True)),
                ('experience_title', models.CharField(max_length=100)),
                ('experience_desc', models.TextField()),
                ('experience_recommendation', models.TextField(null=True)),
                ('experience_start_date', models.DateField(null=True)),
                ('experience_end_date', models.DateField(null=True)),
                ('experience_date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(1, 'APPROVE'), (2, 'KEEP AS DRAFT'), (3, 'REJECT')], default=2)),
                ('website', models.CharField(max_length=100, null=True)),
                ('experience_views', models.IntegerField(default=0)),
                ('organizer_logo_link', models.TextField()),
            ],
        ),
    ]

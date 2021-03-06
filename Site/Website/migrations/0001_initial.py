# Generated by Django 2.0.2 on 2020-04-10 19:26

import Website.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type_event', models.CharField(choices=[('online', 'ONLINE'), ('offline', 'OFFLINE')], default='offline', max_length=50)),
                ('venue', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True)),
                ('time', models.TimeField(blank=True)),
                ('poster', models.ImageField(null=True, upload_to='event_poster')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('year', models.IntegerField(choices=[(1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Final Year')], default=2)),
                ('department', models.CharField(choices=[('OFFICE BEARERS', 'Office Bearers'), ('MANAGEMENT', 'Management'), ('TECHNICAL', 'Technical'), ('WEBD', 'Web Developement'), ('GRAPHICS', 'Graphics and Photography'), ('NDORS', 'NDORS')], default='FIRST', max_length=20)),
                ('post', models.CharField(choices=[('PRESIDENT', 'President'), ('VICE PRESIDENT', 'Vice President'), ('GENERAL SECRETARY', 'General Secretary'), ('TREASURER', 'Treasurer'), ('CONVENER', 'Convener'), ('TECH HEAD', 'Tech Head'), ('DESIGN HEAD', 'Design Head'), ('WEBD', 'web D'), ('PUBLICITY HEAD', 'Publicity Head'), ('CREATIVE HEAD', 'Creative Head'), ('SPONSORSHIP HEAD', 'Sponsorship Head'), ('ACCOMODATION,TRAVEL AND HOSPITALITY HEAD', 'Accomodation,travel and Hospitality Head'), ('BAJA COORDINATOR', 'Baja coordinator'), ('WORKSHOP HEAD', 'Workshop Head'), ('EVENTS HEAD', 'Events Head'), ('EVENTS AND FEST COORDINATOR', 'Events and Fest coordinator'), ('LOGISTIC HEAD', 'Logistic Head'), ('NONE', 'None')], default='None', max_length=40)),
                ('fb', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('photo', models.ImageField(null=True, upload_to='profile_pics', validators=[Website.models.validate_image_size])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

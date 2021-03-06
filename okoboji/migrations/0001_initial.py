# Generated by Django 2.2.5 on 2020-08-12 17:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_date', models.DateField()),
                ('attendees', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

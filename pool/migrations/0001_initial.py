# Generated by Django 3.0.6 on 2020-05-14 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField(help_text='hh:mm am/pm')),
                ('flexibility_before', models.TimeField(help_text='hh:mm am/pm')),
                ('flexibility_after', models.TimeField(help_text='hh:mm am/pm')),
                ('booking_url', models.URLField(default='')),
                ('user_url', models.URLField(default='')),
            ],
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-14 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0003_auto_20200613_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='location',
            field=models.CharField(choices=[('KIA', 'Kempegowda International Airport'), ('MBS', 'Majestic Bus Station'), ('KSR', 'Bangalore City Railway Station (Krantivira Sangolli Rayanna Railway Station)'), ('BCR', 'Bangalore Cantonment Railway Station'), ('YJR', 'Yeshwanthpur Junction Railway Station'), ('KPR', 'KR Puram Railway Station'), ('BMR', 'Baiyapanahalli Metro Station (Purple)'), ('MRM', 'Mysore Road Metro Station (Purple)'), ('NMS', 'Nagasandra Metro Station (Green)'), ('YMS', 'Yelanchenahalli Metro Station (Green)'), ('MMS', 'Majestic Metro Station (Green<->Purple)')], default='KIA', max_length=3),
        ),
    ]

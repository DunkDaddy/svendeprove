# Generated by Django 4.0 on 2023-02-17 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_person_cpr'),
    ]

    operations = [
        migrations.CreateModel(
            name='setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pointThreshold', models.IntegerField(default=500)),
                ('startUpPoints', models.IntegerField(default=300)),
            ],
        ),
    ]

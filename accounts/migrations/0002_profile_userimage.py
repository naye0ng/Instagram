# Generated by Django 2.1.8 on 2019-04-18 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='userimage',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

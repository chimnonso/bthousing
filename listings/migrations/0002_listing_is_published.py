# Generated by Django 3.2.5 on 2021-07-21 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]

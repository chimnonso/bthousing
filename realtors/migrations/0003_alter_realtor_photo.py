# Generated by Django 3.2.5 on 2021-07-22 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_alter_realtor_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='photo/%Y/%m/%d/'),
        ),
    ]
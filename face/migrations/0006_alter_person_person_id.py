# Generated by Django 4.2 on 2023-04-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0005_person_person_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Person_Id',
            field=models.CharField(default='', max_length=10),
        ),
    ]
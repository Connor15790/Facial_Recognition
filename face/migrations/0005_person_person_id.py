# Generated by Django 4.2 on 2023-04-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0004_rename_person_dob_person_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Person_Id',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 4.1 on 2022-10-16 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncard_app', '0036_alter_person_cre_role_alter_person_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='number_attendees',
            field=models.TextField(blank=True, default=0, null=True, verbose_name='number of Attendees'),
        ),
    ]

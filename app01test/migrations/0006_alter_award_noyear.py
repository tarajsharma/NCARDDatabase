# Generated by Django 4.1 on 2022-08-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01test", "0005_award_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="award",
            name="noYear",
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10),
        ),
    ]

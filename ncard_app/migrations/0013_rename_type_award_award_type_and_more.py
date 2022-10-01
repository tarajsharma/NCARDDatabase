# Generated by Django 4.1 on 2022-09-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncard_app', '0008_remove_award_noyear_award_no_year_squashed_0012_alter_award_no_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='award',
            old_name='type',
            new_name='award_type',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='type',
            new_name='event_type',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='type',
            new_name='organisation_type',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='type',
            new_name='publication_type',
        ),
        migrations.AlterField(
            model_name='award',
            name='no_year',
            field=models.DecimalField(blank=True, decimal_places=1, default=1.0, max_digits=10, null=True, verbose_name='Noyear'),
        ),
        migrations.DeleteModel(
            name='PersonAddress',
        ),
    ]
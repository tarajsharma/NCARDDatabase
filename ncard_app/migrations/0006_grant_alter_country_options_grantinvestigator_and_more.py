# Generated by Django 4.1 on 2022-08-27 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ncard_app', '0005_country_organisation_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, max_length=64)),
                ('title', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['code'], 'verbose_name_plural': 'countries'},
        ),
        migrations.CreateModel(
            name='GrantInvestigator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chief', models.BooleanField(default=False)),
                ('grant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ncard_app.grant')),
                ('investigator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ncard_app.person')),
            ],
        ),
        migrations.AddField(
            model_name='grant',
            name='investigators',
            field=models.ManyToManyField(through='ncard_app.GrantInvestigator', to='ncard_app.person'),
        ),
        migrations.AddField(
            model_name='grant',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grants', to='ncard_app.project'),
        ),
        migrations.AddConstraint(
            model_name='grantinvestigator',
            constraint=models.UniqueConstraint(fields=('grant', 'investigator'), name='grantinvestigator_unique'),
        ),
    ]

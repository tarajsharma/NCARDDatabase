# Generated by Django 4.1 on 2022-08-28 13:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app01test", "0002_ncardinfo_profile_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "code",
                    models.CharField(
                        max_length=2,
                        primary_key=True,
                        serialize=False,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[A-Z]{2}$",
                                "Country code must be two upper-case letters, e.g. AU",
                            )
                        ],
                        verbose_name="country code",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
            ],
            options={"verbose_name_plural": "countries", "ordering": ["code"],},
        ),
        migrations.CreateModel(
            name="Grant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reference", models.CharField(blank=True, max_length=64)),
                ("title", models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=16)),
                ("given_name", models.CharField(max_length=64)),
                ("middle_name", models.CharField(blank=True, max_length=64)),
                ("surname", models.CharField(blank=True, max_length=64)),
                ("surname_first", models.BooleanField(default=False)),
                (
                    "auth_user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="person",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "people",
                "ordering": ["surname", "given_name", "id"],
            },
        ),
        migrations.CreateModel(
            name="Publication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=255, verbose_name="type")),
                ("year", models.PositiveSmallIntegerField(verbose_name="year")),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                ("journal", models.CharField(max_length=255, verbose_name="journal")),
                (
                    "journal_ISSN",
                    models.CharField(max_length=255, verbose_name="journal ISSN"),
                ),
                (
                    "volume",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="volume"
                    ),
                ),
                (
                    "page_start",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="start page"
                    ),
                ),
                (
                    "page_end",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="end page"
                    ),
                ),
                (
                    "open_access_status",
                    models.IntegerField(
                        choices=[
                            (0, "None"),
                            (1, "Open"),
                            (2, "Closed"),
                            (3, "Indeterminate"),
                            (4, "Embargoed"),
                        ],
                        default=0,
                    ),
                ),
                ("doi", models.CharField(max_length=255, verbose_name="doi")),
                (
                    "electronic_ISBN",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="electronic ISBN"
                    ),
                ),
                (
                    "print_ISBN",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="print ISBN"
                    ),
                ),
                ("abstract", models.TextField(blank=True, verbose_name="abstract")),
                (
                    "citation",
                    models.TextField(blank=True, verbose_name="citation (Vancouver)"),
                ),
                (
                    "source_ID",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="source ID"
                    ),
                ),
                (
                    "ncard_publication",
                    models.BooleanField(default=True, verbose_name="NCARD publication"),
                ),
                ("contributors", models.ManyToManyField(to="app01test.person")),
            ],
            options={"ordering": ["-year"],},
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "-"),
                            (1, "Pending"),
                            (2, "Active"),
                            (3, "Complete"),
                        ],
                        default=0,
                    ),
                ),
                ("funded", models.BooleanField(default=False)),
                (
                    "lead",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="projects",
                        to="app01test.person",
                    ),
                ),
            ],
            options={"ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="PersonAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.IntegerField(choices=[(1, "Home"), (2, "Work")])),
                ("line1", models.CharField(max_length=64, verbose_name="line 1")),
                (
                    "line2",
                    models.CharField(blank=True, max_length=64, verbose_name="line 2"),
                ),
                (
                    "line3",
                    models.CharField(blank=True, max_length=64, verbose_name="line 3"),
                ),
                ("suburb", models.CharField(blank=True, max_length=32)),
                (
                    "state",
                    models.CharField(
                        blank=True, max_length=3, verbose_name="state (abbrev.)"
                    ),
                ),
                ("postcode", models.CharField(max_length=20)),
                (
                    "country",
                    models.ForeignKey(
                        default="AU",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to="app01test.country",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="addresses",
                        to="app01test.person",
                    ),
                ),
            ],
            options={"verbose_name": "address", "verbose_name_plural": "addresses",},
        ),
        migrations.CreateModel(
            name="Organisation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=25,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[ 0-9()+,*#-]*$",
                                "Phone numbers must contain only these characters: #()*+,-0123456789",
                            )
                        ],
                        verbose_name="phone",
                    ),
                ),
                ("website", models.URLField(blank=True, verbose_name="website")),
                (
                    "twitter_handle",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^$|^@[A-Za-z0-9_]+$",
                                "Twitter handle must begin with an @ and only contain letters, digits and underscores.",
                            )
                        ],
                        verbose_name="Twitter handle",
                    ),
                ),
                (
                    "type",
                    models.IntegerField(
                        choices=[
                            (0, "-"),
                            (1, "Health/Education/Research"),
                            (2, "Funding Agency"),
                            (3, "Community"),
                            (4, "Service Provider"),
                        ],
                        default=0,
                        verbose_name="type",
                    ),
                ),
                (
                    "primary_contact",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="organisations_primary_contact",
                        to="app01test.person",
                    ),
                ),
            ],
            options={"ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="GrantInvestigator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chief", models.BooleanField(default=False)),
                (
                    "grant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="app01test.grant",
                    ),
                ),
                (
                    "investigator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="app01test.person",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="grant",
            name="investigators",
            field=models.ManyToManyField(
                through="app01test.GrantInvestigator", to="app01test.person"
            ),
        ),
        migrations.AddField(
            model_name="grant",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="grants",
                to="app01test.project",
            ),
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=255, verbose_name="type")),
                ("date", models.DateField(verbose_name="date")),
                (
                    "number_attendees",
                    models.IntegerField(verbose_name="number of attendees"),
                ),
                (
                    "title",
                    models.CharField(blank=True, max_length=255, verbose_name="title"),
                ),
                ("detail", models.TextField(verbose_name="detail")),
                ("participants", models.TextField(verbose_name="participants")),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="location"
                    ),
                ),
                (
                    "lead_contacts",
                    models.ManyToManyField(blank=True, to="app01test.person"),
                ),
                (
                    "lead_organisation",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="events",
                        to="app01test.organisation",
                    ),
                ),
            ],
            options={"ordering": ["-date"],},
        ),
        migrations.CreateModel(
            name="ContactRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, verbose_name="email"),
                ),
                (
                    "email2",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email 2"
                    ),
                ),
                (
                    "phone_office",
                    models.CharField(
                        blank=True,
                        max_length=25,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[ 0-9()+,*#-]*$",
                                "Phone numbers must contain only these characters: #()*+,-0123456789",
                            )
                        ],
                        verbose_name="phone (office)",
                    ),
                ),
                (
                    "phone_mobile",
                    models.CharField(
                        blank=True,
                        max_length=25,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[ 0-9()+,*#-]*$",
                                "Phone numbers must contain only these characters: #()*+,-0123456789",
                            )
                        ],
                        verbose_name="phone (mobile)",
                    ),
                ),
                (
                    "phone_home",
                    models.CharField(
                        blank=True,
                        max_length=25,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[ 0-9()+,*#-]*$",
                                "Phone numbers must contain only these characters: #()*+,-0123456789",
                            )
                        ],
                        verbose_name="phone (home)",
                    ),
                ),
                (
                    "cre_role",
                    models.CharField(
                        blank=True, max_length=15, verbose_name="CRE role"
                    ),
                ),
                (
                    "ncard_relation",
                    models.IntegerField(
                        choices=[
                            (1, "Core team"),
                            (2, "Affiliate"),
                            (3, "Collaborator"),
                            (4, "Community / Consumer"),
                            (5, "Advocate"),
                            (6, "Govt / Industry"),
                            (0, "Other"),
                        ],
                        default=0,
                        verbose_name="relationship with NCARD",
                    ),
                ),
                ("project", models.CharField(blank=True, max_length=50)),
                (
                    "display_on_website",
                    models.IntegerField(
                        choices=[(0, "No"), (1, "Yes"), (2, "Yes - student")], default=0
                    ),
                ),
                (
                    "profile_url",
                    models.URLField(blank=True, verbose_name="profile URL"),
                ),
                (
                    "orcid_id",
                    models.CharField(
                        blank=True,
                        max_length=37,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^$|^https://orcid\\.org/\\d{4}-\\d{4}-\\d{4}-\\d{3}(\\d|X)$",
                                "ORCID identifier must be a full URL, in this format: https://orcid.org/XXXX-XXXX-XXXX-XXXX",
                            )
                        ],
                        verbose_name="ORCID iD",
                    ),
                ),
                (
                    "scopus_id",
                    models.BigIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "Value must not be negative."
                            )
                        ],
                        verbose_name="Scopus ID",
                    ),
                ),
                (
                    "wos_researcher_id",
                    models.CharField(
                        blank=True, max_length=32, verbose_name="WoS ResearcherID"
                    ),
                ),
                (
                    "google_scholar",
                    models.URLField(blank=True, verbose_name="Google Scholar"),
                ),
                (
                    "researchgate",
                    models.URLField(blank=True, verbose_name="ResearchGate"),
                ),
                (
                    "loop_profile",
                    models.URLField(blank=True, verbose_name="Loop profile"),
                ),
                ("linkedin", models.URLField(blank=True, verbose_name="LinkedIn")),
                (
                    "twitter",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^$|^@[A-Za-z0-9_]+$",
                                "Twitter handle must begin with an @ and only contain letters, digits and underscores.",
                            )
                        ],
                        verbose_name="Twitter handle",
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=50)),
                ("clinician", models.BooleanField(default=False)),
                ("notes", models.TextField(blank=True)),
                ("research_focus", models.CharField(blank=True, max_length=255)),
                (
                    "employers",
                    models.ManyToManyField(blank=True, to="app01test.organisation"),
                ),
                (
                    "organisation_other",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="contact_records_other",
                        to="app01test.organisation",
                        verbose_name="organisation (other)",
                    ),
                ),
                (
                    "organisation_primary",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="contact_records_primary",
                        to="app01test.organisation",
                        verbose_name="organisation (primary)",
                    ),
                ),
                (
                    "person",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact",
                        to="app01test.person",
                    ),
                ),
            ],
            options={"ordering": ["person"],},
        ),
        migrations.CreateModel(
            name="Award",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.IntegerField(
                        choices=[(1, "Prize"), (2, "Scholarship")], verbose_name="type"
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "status",
                    models.IntegerField(
                        choices=[(1, "Awardee"), (2, "Nominee"), (3, "Finalist")],
                        default=1,
                        verbose_name="award status",
                    ),
                ),
                ("detail", models.TextField(blank=True, verbose_name="detail")),
                ("year", models.PositiveSmallIntegerField(verbose_name="year")),
                (
                    "agency",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="awards",
                        to="app01test.organisation",
                    ),
                ),
                ("recipients", models.ManyToManyField(to="app01test.person")),
            ],
            options={"ordering": ["-year"],},
        ),
        migrations.AddIndex(
            model_name="project",
            index=models.Index(fields=["name"], name="app01test_p_name_cd4910_idx"),
        ),
        migrations.AddIndex(
            model_name="personaddress",
            index=models.Index(
                fields=["person", "type"], name="app01test_p_person__addfd4_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="personaddress",
            constraint=models.UniqueConstraint(
                fields=("person", "type"), name="address_unique_person_type"
            ),
        ),
        migrations.AddIndex(
            model_name="person",
            index=models.Index(
                fields=["surname"], name="app01test_p_surname_c7ae60_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="person",
            index=models.Index(
                fields=["given_name"], name="app01test_p_given_n_895e67_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="grantinvestigator",
            constraint=models.UniqueConstraint(
                fields=("grant", "investigator"), name="grantinvestigator_unique"
            ),
        ),
        migrations.AddIndex(
            model_name="contactrecord",
            index=models.Index(
                fields=["person"], name="app01test_c_person__a2e70d_idx"
            ),
        ),
    ]

# Generated by Django 5.0.7 on 2024-11-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0004_authgroup_authgrouppermissions_authpermission_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoardUni",
            fields=[
                (
                    "board_uni_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("postname", models.CharField(blank=True, max_length=100, null=True)),
                ("content", models.TextField(blank=True, null=True)),
                ("createdate", models.DateTimeField()),
                ("updatedate", models.DateTimeField()),
            ],
            options={
                "db_table": "board_uni",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="AuthGroup",
        ),
        migrations.DeleteModel(
            name="AuthGroupPermissions",
        ),
        migrations.DeleteModel(
            name="AuthPermission",
        ),
        migrations.DeleteModel(
            name="AuthUser",
        ),
        migrations.DeleteModel(
            name="AuthUserGroups",
        ),
        migrations.DeleteModel(
            name="AuthUserUserPermissions",
        ),
        migrations.DeleteModel(
            name="DjangoAdminLog",
        ),
        migrations.DeleteModel(
            name="DjangoContentType",
        ),
        migrations.DeleteModel(
            name="DjangoMigrations",
        ),
        migrations.DeleteModel(
            name="DjangoSession",
        ),
    ]
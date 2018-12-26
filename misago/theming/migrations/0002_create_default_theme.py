# Generated by Django 1.11.16 on 2018-12-26 16:11
from django.db import migrations


def create_default_theme(apps, schema_editor):
    Theme = apps.get_model("misago_theming", "Theme")
    Theme.objects.create(
        name="default",
        is_default=True,
        is_active=True,
        lft=1,
        rght=2,
        tree_id=0,
        level=0,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('misago_theming', '0001_initial'),
    ]

    operations = [migrations.RunPython(create_default_theme)]

# Generated by Django 3.2.16 on 2022-12-24 00:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("submission", "0070_review_uniqueness"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="review",
            unique_together={("user", "submission")},
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_version_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='change',
            name='content',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='version',
            name='content',
            field=models.JSONField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2 on 2024-01-20 10:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='public_policies',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

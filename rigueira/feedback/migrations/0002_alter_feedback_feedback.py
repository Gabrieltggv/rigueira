# Generated by Django 4.1 on 2022-08-10 02:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

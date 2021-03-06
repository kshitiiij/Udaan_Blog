# Generated by Django 3.0.3 on 2020-04-02 13:06

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0016_auto_20200402_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 13, 6, 52, 175054, tzinfo=utc)),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-12 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]
# Generated by Django 4.2.2 on 2023-07-15 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_ticket_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='ticket_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

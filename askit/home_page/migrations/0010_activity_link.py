# Generated by Django 4.1.7 on 2023-04-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0009_rename_notifications_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='link',
            field=models.CharField(default='', max_length=150),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-06 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0006_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='link',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='detail',
            field=models.CharField(max_length=500),
        ),
    ]

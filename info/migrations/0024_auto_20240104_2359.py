# Generated by Django 2.2.16 on 2024-01-04 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0023_remove_message_recaptcha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='facebook',
            new_name='youtube',
        ),
        migrations.RemoveField(
            model_name='information',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='information',
            name='twitter',
        ),
    ]
# Generated by Django 4.2 on 2023-04-15 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_created_at_user_created_on_alter_profile_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='created_on',
            new_name='created_at',
        ),
    ]
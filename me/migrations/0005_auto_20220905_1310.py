# Generated by Django 3.0.5 on 2022-09-05 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0004_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogg',
            old_name='user_id',
            new_name='user',
        ),
    ]

# Generated by Django 3.2.15 on 2022-09-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0015_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogg',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/imagess/'),
        ),
    ]

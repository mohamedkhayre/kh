# Generated by Django 3.2.15 on 2022-10-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0018_auto_20221007_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='exceldata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
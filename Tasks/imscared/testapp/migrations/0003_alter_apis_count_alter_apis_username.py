# Generated by Django 4.1.1 on 2022-09-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_rename_api_apis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apis',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='apis',
            name='username',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]

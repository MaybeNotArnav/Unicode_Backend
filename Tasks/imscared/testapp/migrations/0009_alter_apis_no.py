# Generated by Django 4.1.1 on 2022-09-17 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_alter_apis_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apis',
            name='no',
            field=models.IntegerField(max_length=50),
        ),
    ]
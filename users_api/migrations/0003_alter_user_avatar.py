# Generated by Django 3.2 on 2022-10-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0002_auto_20221020_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.URLField(max_length=300),
        ),
    ]
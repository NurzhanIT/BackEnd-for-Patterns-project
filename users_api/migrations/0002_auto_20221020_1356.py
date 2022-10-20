# Generated by Django 3.2 on 2022-10-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='surname',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='nick',
            field=models.CharField(default='https://reqres.in/img/faces/3-image.jpg', max_length=20),
            preserve_default=False,
        ),
    ]

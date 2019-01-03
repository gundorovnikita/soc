# Generated by Django 2.1.4 on 2019-01-03 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0014_remove_post_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user_profile.Profile'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2 on 2023-04-21 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0002_alter_podcastprogress_paused_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='cover_img',
            field=models.ImageField(null=True, upload_to='cover_img/'),
        ),
    ]
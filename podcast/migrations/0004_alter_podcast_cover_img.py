# Generated by Django 4.2 on 2023-04-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0003_podcast_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='cover_img',
            field=models.ImageField(blank=True, default='cover_img/DSC_0212ps_comp.jpg', null=True, upload_to='cover_img/'),
        ),
    ]

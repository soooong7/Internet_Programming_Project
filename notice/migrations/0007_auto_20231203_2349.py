# Generated by Django 3.1.1 on 2023-12-03 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0006_auto_20231201_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='notice_image',
            field=models.ImageField(blank=True, upload_to='notice/images/%y/%m/%d/'),
        ),
    ]
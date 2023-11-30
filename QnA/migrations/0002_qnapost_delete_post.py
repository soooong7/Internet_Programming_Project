# Generated by Django 4.2.7 on 2023-11-23 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QnAPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

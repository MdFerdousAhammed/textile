# Generated by Django 4.1.1 on 2023-02-12 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beximapp', '0003_post_posted_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]

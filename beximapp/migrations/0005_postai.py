# Generated by Django 4.1.1 on 2023-02-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beximapp', '0004_remove_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts')),
                ('title', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]

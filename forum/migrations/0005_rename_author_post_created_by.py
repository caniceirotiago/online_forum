# Generated by Django 5.1 on 2024-08-21 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='created_by',
        ),
    ]

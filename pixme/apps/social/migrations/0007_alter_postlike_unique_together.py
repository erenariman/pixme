# Generated by Django 4.2.1 on 2023-05-11 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pixme_social', '0006_rename_likes_post_liked_by_alter_postlike_post'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together={('profile', 'post')},
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-21 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('renderer', '0002_remove_poster_url_poster_director_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poster',
            name='director_name',
        ),
    ]
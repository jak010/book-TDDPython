# Generated by Django 3.1.2 on 2021-03-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

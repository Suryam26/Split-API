# Generated by Django 3.2.4 on 2021-07-07 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='name',
            new_name='title',
        ),
        migrations.AddConstraint(
            model_name='bill',
            constraint=models.UniqueConstraint(fields=('title', 'user'), name='unique bill'),
        ),
        migrations.AddConstraint(
            model_name='consumer',
            constraint=models.UniqueConstraint(fields=('name', 'bill'), name='unique user'),
        ),
        migrations.AddConstraint(
            model_name='item',
            constraint=models.UniqueConstraint(fields=('name', 'bill'), name='unique item'),
        ),
    ]

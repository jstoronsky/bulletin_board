# Generated by Django 4.2.4 on 2023-11-08 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0003_alter_advertisement_last_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['-created_at'], 'verbose_name': 'объявление', 'verbose_name_plural': 'объявления'},
        ),
    ]
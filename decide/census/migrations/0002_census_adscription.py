# Generated by Django 2.0 on 2022-10-16 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='census',
            name='adscription',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
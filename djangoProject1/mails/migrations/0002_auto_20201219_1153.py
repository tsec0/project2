# Generated by Django 3.1.4 on 2020-12-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mail',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]

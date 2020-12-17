# Generated by Django 3.1.4 on 2020-12-16 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_auto_20201216_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='IsRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isread', models.CharField(max_length=6)),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mails.mail')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]

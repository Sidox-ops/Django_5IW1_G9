# Generated by Django 3.2.16 on 2022-12-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='name',
            field=models.CharField(default='Library', max_length=100),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.7 on 2023-10-25 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='full_name',
            field=models.CharField(default=3214, max_length=200),
            preserve_default=False,
        ),
    ]

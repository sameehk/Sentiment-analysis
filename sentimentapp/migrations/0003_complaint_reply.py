# Generated by Django 3.2.25 on 2024-03-23 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentapp', '0002_alter_usertable_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='reply',
            field=models.CharField(default=1, max_length=800),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.15 on 2025-05-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(default='kanth', max_length=20),
            preserve_default=False,
        ),
    ]

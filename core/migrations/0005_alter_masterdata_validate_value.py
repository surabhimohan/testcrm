# Generated by Django 4.0.4 on 2022-04-26 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_masterdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterdata',
            name='validate_value',
            field=models.TextField(blank=True, null=True),
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-17 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0002_alter_pessoa_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='idade',
            field=models.IntegerField(null=True),
        ),
    ]

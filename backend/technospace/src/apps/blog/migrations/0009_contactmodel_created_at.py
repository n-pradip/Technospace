# Generated by Django 4.0.5 on 2022-12-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_contactmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
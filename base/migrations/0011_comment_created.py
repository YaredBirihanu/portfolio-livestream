# Generated by Django 3.2.4 on 2021-06-03 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]

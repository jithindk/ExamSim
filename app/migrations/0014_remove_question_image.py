# Generated by Django 3.1.3 on 2021-01-05 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_question_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
    ]

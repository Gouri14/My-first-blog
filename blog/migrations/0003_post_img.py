# Generated by Django 2.2.22 on 2021-05-26 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='images/', upload_to='images/'),
            preserve_default=False,
        ),
    ]

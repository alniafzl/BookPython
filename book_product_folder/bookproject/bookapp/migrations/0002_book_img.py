# Generated by Django 4.1.7 on 2023-04-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(default=1234, upload_to='gallery'),
            preserve_default=False,
        ),
    ]

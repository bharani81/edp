# Generated by Django 4.0.8 on 2023-04-02 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='media\\ocr1.jpg', upload_to='pics'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-26 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='../static/images/bot.jpg', upload_to='profile/'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0002_contact_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='picture',
            field=models.ImageField(default='blank.png', upload_to='profile_img'),
        ),
    ]
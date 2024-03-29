# Generated by Django 4.2.6 on 2023-10-17 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discription',
            new_name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='defaults/hetfield.jpg', null=True, upload_to='products'),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-29 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articel',
            name='Image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]

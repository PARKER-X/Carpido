# Generated by Django 4.0.2 on 2022-06-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_car_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='images2',
            field=models.FileField(blank=True, null=True, upload_to='car'),
        ),
        migrations.AddField(
            model_name='car',
            name='images3',
            field=models.ImageField(blank=True, null=True, upload_to='car'),
        ),
        migrations.AddField(
            model_name='car',
            name='images4',
            field=models.ImageField(blank=True, null=True, upload_to='car'),
        ),
        migrations.AddField(
            model_name='car',
            name='images5',
            field=models.ImageField(blank=True, null=True, upload_to='car'),
        ),
        migrations.AlterField(
            model_name='car',
            name='images',
            field=models.ImageField(blank=True, upload_to='car'),
        ),
    ]

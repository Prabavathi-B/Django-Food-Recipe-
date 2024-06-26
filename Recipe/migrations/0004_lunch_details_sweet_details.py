# Generated by Django 5.0.2 on 2024-05-06 08:55

import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0003_breakfast_details_video_dinner_details_video_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='lunch_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('video', embed_video.fields.EmbedVideoField(default='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='sweet_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('video', embed_video.fields.EmbedVideoField(default='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

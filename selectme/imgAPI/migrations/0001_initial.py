# Generated by Django 3.2.2 on 2021-06-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ImgDate', models.DateField()),
                ('Userid', models.CharField(blank=True, max_length=255)),
                ('Ceremony', models.CharField(blank=True, max_length=255)),
                ('picture', models.ImageField(blank=True, upload_to=models.DateField())),
            ],
        ),
    ]

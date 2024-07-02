# Generated by Django 5.0.6 on 2024-06-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('X', 'X'), ('INSTAGRAM', 'Instagram'), ('YOUTUBE', 'Youtube'), ('BLOG', 'Blog')], max_length=10)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

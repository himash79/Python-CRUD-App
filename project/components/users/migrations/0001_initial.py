# Generated by Django 4.2.7 on 2023-11-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
# Generated by Django 2.0.6 on 2018-07-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(max_length=256, unique=True)),
                ('course_description', models.TextField(max_length=1024, unique=True)),
            ],
        ),
    ]

# Generated by Django 2.0.6 on 2018-07-08 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180708_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedescription',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='courses.Course'),
        ),
    ]

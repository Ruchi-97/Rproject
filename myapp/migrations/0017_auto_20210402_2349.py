# Generated by Django 3.1.2 on 2021-04-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_clickcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickcount',
            name='count',
            field=models.IntegerField(default=3),
        ),
    ]

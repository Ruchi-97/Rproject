# Generated by Django 3.1.2 on 2021-03-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20210324_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='level3',
            name='img_name',
            field=models.CharField(default='', max_length=60),
        ),
    ]

# Generated by Django 4.0 on 2022-02-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0003_tag_anime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='type',
            field=models.CharField(max_length=7),
        ),
    ]

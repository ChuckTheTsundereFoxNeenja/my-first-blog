# Generated by Django 2.2.15 on 2020-08-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20200827_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='finished_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='started_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='finished_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='started_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

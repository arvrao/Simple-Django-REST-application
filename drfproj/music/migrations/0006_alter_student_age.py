# Generated by Django 3.2.5 on 2021-07-22 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-21 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_subject_tc'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeSub',
            fields=[
                ('type_id', models.BooleanField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=100)),
            ],
        ),
    ]

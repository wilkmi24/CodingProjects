# Generated by Django 3.1.3 on 2020-11-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, default='', max_length=60)),
                ('Course', models.IntegerField(blank=True, null=True)),
                ('Instructor', models.CharField(blank=True, default='', max_length=60)),
                ('Duration', models.FloatField(default='')),
            ],
        ),
    ]

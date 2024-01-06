# Generated by Django 4.2.5 on 2024-01-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totsp', models.IntegerField()),
                ('livesp', models.IntegerField()),
                ('kitsp', models.IntegerField()),
                ('dist', models.IntegerField()),
                ('metrdist', models.IntegerField()),
                ('walk', models.BooleanField()),
                ('brick', models.BooleanField()),
                ('floor', models.BooleanField()),
            ],
        ),
    ]

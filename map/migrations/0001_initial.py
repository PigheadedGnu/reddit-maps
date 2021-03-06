# Generated by Django 3.1.6 on 2021-02-13 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reddit_id', models.CharField(max_length=255)),
                ('map', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.map')),
            ],
        ),
    ]

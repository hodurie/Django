# Generated by Django 3.1 on 2020-08-28 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]

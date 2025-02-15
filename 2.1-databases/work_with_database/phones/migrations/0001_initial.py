# Generated by Django 4.0.2 on 2022-02-13 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('release_date', models.DateTimeField()),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]

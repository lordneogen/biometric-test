# Generated by Django 4.2.5 on 2023-09-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('iin', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Персона',
                'verbose_name_plural': 'Персоны',
                'db_table': 'persons',
                'managed': True,
            },
        ),
    ]

# Generated by Django 5.0 on 2024-02-06 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Module1', '0002_alter_register_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('feedback_text', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]

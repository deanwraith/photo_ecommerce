# Generated by Django 3.2 on 2022-09-19 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20220919_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
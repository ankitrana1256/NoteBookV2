# Generated by Django 3.1.7 on 2021-03-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210302_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
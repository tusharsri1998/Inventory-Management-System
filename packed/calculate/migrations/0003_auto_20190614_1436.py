# Generated by Django 2.2.2 on 2019-06-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0002_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='entry_date',
            field=models.DateField(),
        ),
    ]
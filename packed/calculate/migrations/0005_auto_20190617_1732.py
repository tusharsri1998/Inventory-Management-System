# Generated by Django 2.2.2 on 2019-06-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0004_auto_20190617_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='box_type_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='box_type',
            field=models.IntegerField(default=1, null=True),
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-02 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20191202_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
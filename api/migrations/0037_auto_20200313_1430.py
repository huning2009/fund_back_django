# Generated by Django 3.0 on 2020-03-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_asset_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bondholding',
            name='update_date',
            field=models.DateField(default='2020-01-31', verbose_name='更新时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockholding',
            name='update_date',
            field=models.DateField(default='2020-01-31', verbose_name='更新时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bondholding',
            name='date',
            field=models.DateField(verbose_name='报告期'),
        ),
        migrations.AlterField(
            model_name='stockholding',
            name='date',
            field=models.DateField(verbose_name='报告期'),
        ),
    ]

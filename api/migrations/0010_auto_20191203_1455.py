# Generated by Django 2.2.7 on 2019-12-03 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20191203_1439'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ManagerExtend',
            new_name='ManagerExpand',
        ),
        migrations.AlterField(
            model_name='manager',
            name='fund_fundmanager',
            field=models.CharField(max_length=20, null=True, verbose_name='基金经理'),
        ),
    ]
# Generated by Django 2.2.1 on 2019-07-18 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ericainfo', '0004_auto_20190718_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='locate',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='num',
            field=models.CharField(default='000-0000-0000', max_length=15),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='cate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ericainfo.Category'),
        ),
    ]

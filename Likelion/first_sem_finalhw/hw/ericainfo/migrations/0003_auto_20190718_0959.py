# Generated by Django 2.2.1 on 2019-07-18 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ericainfo', '0002_auto_20190718_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='exid',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='cate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ericainfo.Category'),
        ),
    ]
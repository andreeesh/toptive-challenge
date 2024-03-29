# Generated by Django 3.0.7 on 2020-06-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200630_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='areaname',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='code',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='countryofbirth',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='dateofbirth',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='nationality',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='areaname',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='shortname',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='tla',
            field=models.CharField(max_length=60, null=True),
        ),
    ]

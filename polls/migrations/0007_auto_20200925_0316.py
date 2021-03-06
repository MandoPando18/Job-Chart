# Generated by Django 3.0 on 2020-09-25 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200925_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='denied',
            field=models.IntegerField(choices=[(1, 'Y'), (0, 'N')], default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='offer',
            field=models.IntegerField(choices=[(1, 'Y'), (0, 'N')], default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='phoneinterview',
            field=models.IntegerField(choices=[(1, 'Y'), (0, 'N')], default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='response',
            field=models.IntegerField(choices=[(1, 'Y'), (0, 'N')], default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='test',
            field=models.IntegerField(choices=[(1, 'Y'), (0, 'N')], default=0),
        ),
    ]

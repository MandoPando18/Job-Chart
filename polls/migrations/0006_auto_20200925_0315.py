# Generated by Django 3.0 on 2020-09-25 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200925_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='denied',
            field=models.IntegerField(choices=[(1, 'Y'), (0, 'N')], default='NO'),
        ),
        migrations.AlterField(
            model_name='company',
            name='offer',
            field=models.IntegerField(choices=[(1, 'Y'), (0, 'N')], default='NO'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phoneinterview',
            field=models.IntegerField(choices=[(1, 'Y'), (0, 'N')], default='NO'),
        ),
        migrations.AlterField(
            model_name='company',
            name='test',
            field=models.IntegerField(choices=[(1, 'Y'), (0, 'N')], default='NO'),
        ),
    ]

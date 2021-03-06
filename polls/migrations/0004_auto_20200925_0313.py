# Generated by Django 3.0 on 2020-09-25 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200924_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='denied',
            field=models.CharField(choices=[(1, 'Y'), (0, 'N')], default='NO', max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='offer',
            field=models.CharField(choices=[(1, 'Y'), (0, 'N')], default='NO', max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='phoneinterview',
            field=models.CharField(choices=[(1, 'Y'), (0, 'N')], default='NO', max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='response',
            field=models.CharField(choices=[(1, 'Y'), (0, 'N')], default='NO', max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='test',
            field=models.CharField(choices=[(1, 'Y'), (0, 'N')], default='NO', max_length=20),
        ),
    ]

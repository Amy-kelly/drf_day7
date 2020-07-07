# Generated by Django 3.0.8 on 2020-07-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('kinds', models.CharField(max_length=32, verbose_name='种类')),
            ],
            options={
                'verbose_name': '咖啡',
                'verbose_name_plural': '咖啡',
                'db_table': 'tb_coffee',
            },
        ),
    ]

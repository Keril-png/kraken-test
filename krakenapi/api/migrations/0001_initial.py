# Generated by Django 3.2.9 on 2021-12-01 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair_name', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=3)),
                ('time', models.DateTimeField()),
                ('close', models.FloatField()),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('volume', models.FloatField()),
            ],
        ),
    ]
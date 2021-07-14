# Generated by Django 3.0.7 on 2021-07-14 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0002_auto_20210714_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutosCreate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.IntegerField()),
                ('comments', models.CharField(max_length=200, null=True)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.MakeCreate')),
            ],
        ),
    ]

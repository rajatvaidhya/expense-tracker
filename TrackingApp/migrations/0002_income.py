# Generated by Django 4.0.5 on 2022-07-05 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrackingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=10)),
                ('Time', models.CharField(max_length=10)),
                ('Source', models.CharField(max_length=10)),
                ('Amount', models.CharField(max_length=10)),
                ('Remark', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrackingApp.user')),
            ],
            options={
                'db_table': 'Income',
            },
        ),
    ]

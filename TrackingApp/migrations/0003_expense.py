# Generated by Django 4.0.5 on 2022-07-05 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrackingApp', '0002_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=10)),
                ('Time', models.CharField(max_length=10)),
                ('Amount', models.CharField(max_length=10)),
                ('Expenses', models.CharField(max_length=10)),
                ('Remark', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrackingApp.user')),
            ],
            options={
                'db_table': 'Expense',
            },
        ),
    ]

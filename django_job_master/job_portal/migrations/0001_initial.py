# Generated by Django 2.2 on 2020-01-12 10:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=150)),
                ('type', models.CharField(choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=10)),
                ('category', models.CharField(max_length=100)),
                ('last_date', models.DateTimeField()),
                ('company_name', models.CharField(max_length=100)),
                ('company_description', models.CharField(max_length=300)),
                ('website', models.CharField(default='', max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('filled', models.BooleanField(default=False)),
                ('salary', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
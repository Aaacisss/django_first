# Generated by Django 4.0.5 on 2023-02-17 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Choice_text', models.CharField(default=0, max_length=200)),
                ('gender', models.CharField(default=0, max_length=10)),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_project.question')),
            ],
        ),
    ]

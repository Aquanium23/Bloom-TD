# Generated by Django 4.2.2 on 2023-06-13 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
    ]

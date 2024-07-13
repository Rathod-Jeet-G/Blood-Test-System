# Generated by Django 5.0.6 on 2024-07-06 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0002_alter_userregister_user_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_feedback', models.DateField(auto_created=True, auto_now=True)),
                ('username', models.CharField(default='', max_length=30, verbose_name='Patient Name')),
                ('useremail', models.EmailField(max_length=50, verbose_name='Patient Email')),
                ('feedback', models.TextField(verbose_name='Patient feedback Area')),
            ],
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
        ),
    ]
#at this point, use command 'python manage.py migrate' to update these information(migrations file,model) on our database , and it will create table for us
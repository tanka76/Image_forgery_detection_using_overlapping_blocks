# Generated by Django 3.0.5 on 2020-04-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=50)),
                ('email_id', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='home/sujan/PycharmProjects/learndjango/image_forgery/accounts/media/image')),
            ],
        ),
    ]

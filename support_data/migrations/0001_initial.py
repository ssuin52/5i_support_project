<<<<<<< HEAD
# Generated by Django 4.1.2 on 2022-10-20 00:20
=======
# Generated by Django 4.1.2 on 2022-10-19 23:35
>>>>>>> 790323f1bb8ae9cf4fb1f3402e6d28fb89fcc2ea

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('people_num', models.CharField(max_length=128)),
                ('input_num', models.CharField(max_length=128)),
                ('is_approval', models.BooleanField(default=False)),
                ('write_image', models.ImageField(upload_to='write_images/')),
<<<<<<< HEAD
                ('content', models.CharField(max_length=256)),
=======
>>>>>>> 790323f1bb8ae9cf4fb1f3402e6d28fb89fcc2ea
            ],
            options={
                'db_table': 'support',
            },
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallaries/')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

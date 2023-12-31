# Generated by Django 4.2.6 on 2023-10-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Home and Garden', 'Home and Garden'), ('Toys', 'Toys'), ('Sports and Outdoors', 'Sports and Outdoors')], max_length=50)),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-24 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_category'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItems',
            new_name='CartItem',
        ),
    ]

# Generated by Django 4.1.2 on 2023-01-21 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_produit_tag_produit_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Marque',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='tag',
            new_name='marque',
        ),
    ]
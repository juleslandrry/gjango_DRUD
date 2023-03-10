# Generated by Django 4.0.3 on 2022-10-11 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='tag',
            field=models.ManyToManyField(to='product.tag'),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-30 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petSalud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
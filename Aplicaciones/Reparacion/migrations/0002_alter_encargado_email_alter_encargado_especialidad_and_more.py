# Generated by Django 5.1.5 on 2025-02-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reparacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encargado',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='encargado',
            name='especialidad',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='encargado',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_encargados/'),
        ),
        migrations.AlterField(
            model_name='encargado',
            name='telefono',
            field=models.CharField(max_length=15),
        ),
    ]

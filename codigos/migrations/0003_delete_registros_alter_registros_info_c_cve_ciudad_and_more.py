# Generated by Django 4.2.7 on 2023-11-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codigos', '0002_registros_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registros',
        ),
        migrations.AlterField(
            model_name='registros_info',
            name='c_cve_ciudad',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registros_info',
            name='c_estado',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registros_info',
            name='c_mnpio',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registros_info',
            name='c_tipo_asenta',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registros_info',
            name='id_asenta_cpcons',
            field=models.CharField(max_length=6),
        ),
    ]
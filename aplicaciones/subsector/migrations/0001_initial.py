# Generated by Django 2.0.7 on 2018-07-18 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subsector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsectorCod', models.CharField(max_length=15, unique=True)),
                ('subsectorDescripcion', models.CharField(max_length=50)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sector.Sector')),
            ],
        ),
    ]
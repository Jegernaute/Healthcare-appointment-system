# Generated by Django 5.0.2 on 2024-02-13 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldata',
            name='name_city',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='name_street',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='number_apartment',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='number_house',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='personaldata',
            name='middle_name',
        ),
        migrations.DeleteModel(
            name='NameCity',
        ),
        migrations.DeleteModel(
            name='NameStreet',
        ),
        migrations.DeleteModel(
            name='NumberApartment',
        ),
        migrations.DeleteModel(
            name='NumberHouse',
        ),
    ]
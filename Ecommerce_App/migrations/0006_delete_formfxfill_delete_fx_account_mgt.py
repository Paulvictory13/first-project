# Generated by Django 5.1 on 2024-09-04 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_App', '0005_formfxfill_delete_school'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Formfxfill',
        ),
        migrations.DeleteModel(
            name='Fx_Account_MGT',
        ),
    ]

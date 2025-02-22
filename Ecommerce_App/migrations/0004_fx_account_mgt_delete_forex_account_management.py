# Generated by Django 5.0.7 on 2024-08-16 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_App', '0003_alter_forex_account_management_login_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fx_Account_MGT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_Name', models.CharField(max_length=50)),
                ('Email_Address', models.CharField(max_length=50)),
                ('Login', models.IntegerField()),
                ('Trading_Password', models.CharField(max_length=15)),
                ('Meta_Trader', models.CharField(max_length=15)),
                ('Date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Forex_Account_Management',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-23 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnb_kingdom_api', '0003_alter_buyhistory_amount_bnb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyhistory',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnb_kingdom_api', '0002_alter_buyhistory_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyhistory',
            name='amount_bnb',
            field=models.FloatField(),
        ),
    ]

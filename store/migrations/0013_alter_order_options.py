# Generated by Django 5.2.4 on 2025-07-10 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_customer_email_remove_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can cancel order'), ('refund_order', 'Can refund order')]},
        ),
    ]

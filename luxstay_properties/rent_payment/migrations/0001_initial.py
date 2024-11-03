# Generated by Django 5.1.1 on 2024-11-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('paymentId', models.AutoField(primary_key=True, serialize=False)),
                ('lease_id', models.CharField(max_length=50)),
                ('tenant_id', models.CharField(max_length=100)),
                ('paymentDate', models.DateField()),
                ('paymentMethod', models.CharField(max_length=100)),
                ('totalAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]

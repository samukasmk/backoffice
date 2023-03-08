# Generated by Django 4.1.7 on 2023-03-08 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerCommissionPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('New', 'new'), ('Approved', 'approved'), ('Reproved', 'reproved'), ('Payed', 'payed')], max_length=30)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.order')),
            ],
        ),
        migrations.CreateModel(
            name='RoyaltiesPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('New', 'new'), ('Approved', 'approved'), ('Reproved', 'reproved'), ('Payed', 'payed')], max_length=30)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.order')),
            ],
        ),
    ]

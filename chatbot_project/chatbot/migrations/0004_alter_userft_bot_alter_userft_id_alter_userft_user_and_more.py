# Generated by Django 5.0.6 on 2024-07-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_alter_userft_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userft',
            name='bot',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userft',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userft',
            name='user',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='userft',
            table=None,
        ),
    ]

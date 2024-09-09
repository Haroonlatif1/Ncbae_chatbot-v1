# Generated by Django 5.0.6 on 2024-07-10 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_alter_userft_bot_alter_userft_id_alter_userft_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserFT',
            new_name='UserFeedback',
        ),
        migrations.AlterModelOptions(
            name='userfeedback',
            options={'verbose_name_plural': 'User Feedback'},
        ),
        migrations.RenameField(
            model_name='userfeedback',
            old_name='bot',
            new_name='bot_response',
        ),
        migrations.RenameField(
            model_name='userfeedback',
            old_name='user',
            new_name='user_message',
        ),
        migrations.AlterModelTable(
            name='userfeedback',
            table='user_feedback',
        ),
    ]

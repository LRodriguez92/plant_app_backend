# Generated by Django 3.1.3 on 2020-11-14 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201112_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='test@test.com', max_length=100),
            preserve_default=False,
        ),
    ]

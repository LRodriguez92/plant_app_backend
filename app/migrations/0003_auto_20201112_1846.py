# Generated by Django 3.1.3 on 2020-11-12 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201112_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='id',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='plant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='schedule', serialize=False, to='app.plant'),
        ),
    ]
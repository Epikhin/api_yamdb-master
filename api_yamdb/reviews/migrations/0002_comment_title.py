# Generated by Django 3.2 on 2023-02-11 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '__first__'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='catalog.title'),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2.7 on 2022-02-15 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211028_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('i', 'Investigating'), ('r', 'Returned')], max_length=1),
        ),
    ]

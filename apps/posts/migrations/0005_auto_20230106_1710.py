# Generated by Django 3.0 on 2023-01-06 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220916_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postviews',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
    ]
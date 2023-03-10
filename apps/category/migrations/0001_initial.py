# Generated by Django 3.0 on 2022-09-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('category_img', models.ImageField(blank=True, upload_to='')),
                ('category_type', models.CharField(choices=[('world', 'World'), ('environment', 'Environment'), ('technology', 'Technology'), ('design', 'Design'), ('culture', 'Culture'), ('business', 'Business'), ('politics', 'Politics'), ('opinion', 'Opinion'), ('science', 'Science'), ('health', 'Health'), ('style', 'Style'), ('travel', 'Travel'), ('others', 'Others')], default='world', max_length=100)),
            ],
        ),
    ]

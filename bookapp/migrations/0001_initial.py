# Generated by Django 3.1.2 on 2020-11-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('isbn', models.CharField(blank=True, max_length=255, null=True)),
                ('authors', models.CharField(blank=True, max_length=255, null=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('released', models.CharField(blank=True, max_length=255, null=True)),
                ('numberOfPages', models.IntegerField(max_length=10)),
            ],
        ),
    ]
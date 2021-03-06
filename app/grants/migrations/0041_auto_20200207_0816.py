# Generated by Django 2.2.4 on 2020-02-07 08:16

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0040_auto_20200205_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrantCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('category', models.CharField(help_text='Grant Category', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='grant',
            name='categories',
            field=models.ManyToManyField(to='grants.GrantCategory'),
        ),
    ]

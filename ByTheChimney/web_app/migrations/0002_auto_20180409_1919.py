# Generated by Django 2.0.3 on 2018-04-10 00:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('recurring', models.BooleanField()),
                ('location', models.CharField(max_length=75)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('createDate', models.DateTimeField()),
                ('rainDate', models.DateTimeField()),
                ('isDelayed', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='CustomerName',
            new_name='firstName',
        ),
        migrations.AddField(
            model_name='purchase',
            name='lastName',
            field=models.CharField(default='Anon', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(choices=[('3-braid', '3-braid'), ('4-braid', '4-braid')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.CharField(choices=[('Mermaid Tail', 'Mermaid Tail'), ('Dinosaur Tail', 'Dinosaur Tail'), ('Dog Toy', 'Dog Toy'), ('Cat Toy', 'Cat Toy'), ('Cape', 'Cape'), ('Tu-Tu', 'Tu-Tu')], max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]

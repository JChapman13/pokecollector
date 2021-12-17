# Generated by Django 3.2.9 on 2021-12-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_healing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('main_stat', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='healing',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='healing',
            name='date',
            field=models.DateField(verbose_name='healing date'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='armor',
            field=models.ManyToManyField(to='main_app.Armor'),
        ),
    ]

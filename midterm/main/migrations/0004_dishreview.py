# Generated by Django 2.1.1 on 2018-10-12 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181012_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Dish')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Person')),
            ],
        ),
    ]

# Generated by Django 4.0 on 2021-12-12 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='articleA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.article'),
        ),
    ]

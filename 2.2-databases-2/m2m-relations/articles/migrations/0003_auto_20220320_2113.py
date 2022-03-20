# Generated by Django 3.2.12 on 2022-03-20 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20220317_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='tag',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='articlescope',
            name='scope',
        ),
        migrations.AddField(
            model_name='articlescope',
            name='tag',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.scope'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
    ]

# Generated by Django 4.1.6 on 2023-03-06 20:40

from django.db import migrations, models
import django.db.models.deletion
import lab1p.models


class Migration(migrations.Migration):

    dependencies = [
        ('lab1p', '0025_alter_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='adder',
        ),
        migrations.AlterField(
            model_name='book',
            name='Information',
            field=models.TextField(blank=True, default='No info', max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_books', to='lab1p.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='collections',
            field=models.ManyToManyField(blank=True, related_name='books_for_collection', to='lab1p.collection'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13, unique=True, validators=[lab1p.models.validate_isbn], verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='Information',
            field=models.CharField(blank=True, default='No info', max_length=150),
        ),
    ]
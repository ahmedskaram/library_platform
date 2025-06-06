# Generated by Django 5.1.5 on 2025-05-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='books/pdfs/'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['title'], name='Book_book_title_d19049_idx'),
        ),
    ]

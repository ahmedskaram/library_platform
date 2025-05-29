from django.db import models

BATCH_CHOICES = [
    ('year1', 'الفرقة الأولى'),
    ('year2', 'الفرقة الثانية'),
    ('year3', 'الفرقة الثالثة'),
    ('year4', 'الفرقة الرابعة'),
]

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    pdf_file = models.FileField(upload_to='books/pdfs/', null=True, blank=True)
    batch = models.CharField(max_length=10, choices=BATCH_CHOICES, default='year1')

    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=['title'])]

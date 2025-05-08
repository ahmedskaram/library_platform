from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date','description', 'batch', 'pdf_file']
        labels = {
            'title': 'العنوان',
            'author': 'المؤلف',
            'publication_date': 'تاريخ النشر',
            'description': 'الوصف',
            'batch': 'الفرقة',
            'pdf_file': 'تحميل الملف'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل عنوان الكتاب'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل اسم المؤلف'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الوصف'}),
            'batch': forms.Select(attrs={'class': 'form-control'}),
            'pdf_file': forms.FileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
        }

    def clean_pdf_file(self):
        pdf_file = self.cleaned_data.get('pdf_file')
        if pdf_file:
            if not pdf_file.name.endswith('.pdf'):
                raise forms.ValidationError('الملف يجب أن يكون بصيغة PDF.')
        return pdf_file

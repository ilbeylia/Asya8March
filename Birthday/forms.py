from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'text']

    def clean_name(self):
        name = self.cleaned_data['name']
        # Aynı isimle başka bir giriş var mı kontrol et
        if Entry.objects.filter(name=name).exists():
            raise forms.ValidationError("Bu isimle daha önce bir giriş yapılmış.")
        return name
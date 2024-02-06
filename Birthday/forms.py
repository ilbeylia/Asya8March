from django import forms
from .models import Entry
import random

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'text', 'selected_gif', 'point_X', 'point_Y']

    def clean_name(self):
        name = self.cleaned_data['name']
        # Aynı isimle başka bir giriş var mı kontrol et
        if Entry.objects.filter(name=name).exists():
            raise forms.ValidationError("Bu isimle daha önce bir giriş yapılmış.")
        return name

    def clean(self):
        cleaned_data = super().clean()

        # Her eklemde yeni bir point_X ve point_Y değeri oluştur
        cleaned_data['point_X'] = self.generate_random_value('X')
        cleaned_data['point_Y'] = self.generate_random_value('Y')

        return cleaned_data

    def generate_random_value(self, coordinate):
        # Belirtilen koordinata göre rastgele bir sayı oluştur
        if coordinate == 'X':
            existing_values = Entry.objects.values_list('point_X', flat=True)
            random_number = self.generate_x_value(existing_values)
        elif coordinate == 'Y':
            existing_values = Entry.objects.values_list('point_Y', flat=True)
            random_number = self.generate_y_value()
        else:
            raise ValueError("Geçersiz koordinat")

        return random_number

    def generate_x_value(self, existing_values):
        # X değeri 40-60 aralığına dahil olmayan bir rastgele sayı üret
        random_number = random.uniform(10, 90)
        while 40 <= random_number <= 60 or random_number in existing_values:
            random_number = random.uniform(10, 90)
        return random_number

    def generate_y_value(self):
        # Y değeri -25-50 aralığından farklı bir rastgele sayı üret
        return random.uniform(-25, 50)

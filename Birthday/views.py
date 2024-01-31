from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def home(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()

    entries = Entry.objects.all()
    return render(request, 'home.html', {'entries': entries, 'form': form})


def delete_entry_by_name(request, entry_name):
    entry = Entry.objects.get(name=entry_name)
    entry.delete()
    return redirect('home')

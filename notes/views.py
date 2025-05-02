from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/home.html', {'notes': notes})

@login_required
def create_note(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        note = form.save(commit=False)
        note.user = request.user
        note.save()
        return redirect('home')
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def update_note(request, pk):
    note = Note.objects.get(pk=pk, user=request.user)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def delete_note(request, pk):
    note = Note.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    return render(request, 'notes/confirm_delete.html', {'note': note})
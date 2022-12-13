from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from library.models import Genre

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['name', "description"]

def genre_list(request, template_name='genres/genre_list.html'):
    genre = Genre.objects.all()
    data = {}
    data['object_list'] = genre
    return render(request, template_name, data)

def genre_view(request, pk, template_name='genres/genre_detail.html'):
    genre= get_object_or_404(Genre, pk=pk)    
    return render(request, template_name, {'object':genre})

def genre_create(request, template_name='genres/genre_form.html'):
    form = GenreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('genre_list')
    return render(request, template_name, {'form':form})

def genre_update(request, pk, template_name='genres/genre_form.html'):
    genre= get_object_or_404(Genre, pk=pk)
    form = GenreForm(request.POST or None, instance=genre)
    if form.is_valid():
        form.save()
        return redirect('genre_list')
    return render(request, template_name, {'form':form})

def genre_delete(request, pk, template_name='genres/genre_confirm_delete.html'):
    genre= get_object_or_404(Genre, pk=pk)    
    if request.method=='POST':
        genre.delete()
        return redirect('genre_list')
    return render(request, template_name, {'object':genre})
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from library.models import Author

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', "surname"]

def author_list(request, template_name='authors/author_list.html'):
    author = Author.objects.all()
    data = {}
    data['object_list'] = author
    return render(request, template_name, data)

def author_view(request, pk, template_name='authors/author_detail.html'):
    author= get_object_or_404(Author, pk=pk)    
    return render(request, template_name, {'object':author})

def author_create(request, template_name='authors/author_form.html'):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('author_list')
    return render(request, template_name, {'form':form})

def author_update(request, pk, template_name='authors/author_form.html'):
    author= get_object_or_404(Author, pk=pk)
    form = AuthorForm(request.POST or None, instance=author)
    if form.is_valid():
        form.save()
        return redirect('author_list')
    return render(request, template_name, {'form':form})

def author_delete(request, pk, template_name='authors/author_confirm_delete.html'):
    author= get_object_or_404(Author, pk=pk)    
    if request.method=='POST':
        author.delete()
        return redirect('author_list')
    return render(request, template_name, {'object':author})
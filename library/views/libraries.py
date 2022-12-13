from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from library.models import Library

class LibraryForm(ModelForm):
    class Meta:
        model = Library
        fields = ['name', "address","city","zipcode"]

def library_list(request, template_name='libraries/library_list.html'):
    library = Library.objects.all()
    data = {}
    data['object_list'] = library
    return render(request, template_name, data)

def library_view(request, pk, template_name='libraries/library_detail.html'):
    library= get_object_or_404(Library, pk=pk)    
    return render(request, template_name, {'object':library})

def library_create(request, template_name='libraries/library_form.html'):
    form = LibraryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('library_list')
    return render(request, template_name, {'form':form})

def library_update(request, pk, template_name='libraries/library_form.html'):
    library= get_object_or_404(Library, pk=pk)
    form = LibraryForm(request.POST or None, instance=library)
    if form.is_valid():
        form.save()
        return redirect('library_list')
    return render(request, template_name, {'form':form})

def library_delete(request, pk, template_name='libraries/library_confirm_delete.html'):
    library= get_object_or_404(Library, pk=pk)    
    if request.method=='POST':
        library.delete()
        return redirect('library_list')
    return render(request, template_name, {'object':library})
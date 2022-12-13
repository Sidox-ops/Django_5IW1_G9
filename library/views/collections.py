from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from library.models import Collection

class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = ['name', "description"]

def collection_list(request, template_name='collections/collection_list.html'):
    collection = Collection.objects.all()
    data = {}
    data['object_list'] = collection
    return render(request, template_name, data)

def collection_view(request, pk, template_name='collections/collection_detail.html'):
    collection= get_object_or_404(Collection, pk=pk)    
    return render(request, template_name, {'object':collection})

def collection_create(request, template_name='collections/collection_form.html'):
    form = CollectionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('collection_list')
    return render(request, template_name, {'form':form})

def collection_update(request, pk, template_name='collections/collection_form.html'):
    collection= get_object_or_404(Collection, pk=pk)
    form = CollectionForm(request.POST or None, instance=collection)
    if form.is_valid():
        form.save()
        return redirect('collection_list')
    return render(request, template_name, {'form':form})

def collection_delete(request, pk, template_name='collections/collection_confirm_delete.html'):
    collection= get_object_or_404(Collection, pk=pk)    
    if request.method=='POST':
        collection.delete()
        return redirect('collection_list')
    return render(request, template_name, {'object':collection})
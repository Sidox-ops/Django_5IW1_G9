from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from library.models import Editor

class EditorForm(ModelForm):
    class Meta:
        model = Editor
        fields = ['name', "address","phone","email"]

def editor_list(request, template_name='editors/editor_list.html'):
    editor = Editor.objects.all()
    data = {}
    data['object_list'] = editor
    return render(request, template_name, data)

def editor_view(request, pk, template_name='editors/editor_detail.html'):
    editor= get_object_or_404(Editor, pk=pk)    
    return render(request, template_name, {'object':editor})

def editor_create(request, template_name='editors/editor_form.html'):
    form = EditorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('editor_list')
    return render(request, template_name, {'form':form})

def editor_update(request, pk, template_name='editors/editor_form.html'):
    editor= get_object_or_404(Editor, pk=pk)
    form = EditorForm(request.POST or None, instance=editor)
    if form.is_valid():
        form.save()
        return redirect('editor_list')
    return render(request, template_name, {'form':form})

def editor_delete(request, pk, template_name='editors/editor_confirm_delete.html'):
    editor= get_object_or_404(Editor, pk=pk)    
    if request.method=='POST':
        editor.delete()
        return redirect('editor_list')
    return render(request, template_name, {'object':editor})
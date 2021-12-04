from django.db.models.fields.json import DataContains
from django.shortcuts import redirect, render
from .forms import Comments_Form
from .models import comments
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "base/index.html")

@login_required
def Comments(request):
    data = {
        'form' : Comments_Form()
    }
    if request.method == 'POST':
        comentario = Comments_Form(data=request.POST)
        if comentario.is_valid():
            comentario.save()
            return redirect('Home')
        else:
            data['form'] = comentario

    return render(request, 'base/form.html', data)
@login_required
def Comment_List(request):
    comentario = comments.objects.all().order_by('id')
    contexto = {'comentarios':comentario}
    return render(request, 'base/list_comments.html', contexto)

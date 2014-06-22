from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from todo.models import Item

# Create your views here.

def index(request):
    return render(request, 'index.html', dictionary={ 'items': Item.objects.all() })

def complete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.completed = not item.completed
    item.save()

    return HttpResponseRedirect(reverse('todo.views.index'))

def add_item(request):
    try:
        item = Item(title=request.POST['title'])
    except KeyError:
        return HttpResponseRedirect(reverse('todo.views.index'))
    else:
        item.save()
        return HttpResponseRedirect(reverse('todo.views.index'))

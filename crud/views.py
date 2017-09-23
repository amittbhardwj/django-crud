from django.shortcuts import render

# Create your views here.
from .models import CRUD
from .forms import CRUDForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class CRUDList(ListView):
    model = CRUD

    def get_queryset(self):
        result = super(CRUDList, self).get_queryset()
        category = self.request.GET.get('category')
        if category:
            if self.request.GET:
                if self.request.GET.get('asc'):
                    result = CRUD.objects.order_by(category)
                elif self.request.GET.get('desc'):
                   result = CRUD.objects.order_by('-'+category)

        return result

class CRUDCreate(CreateView):
    model = CRUD
    form_class = CRUDForm
    success_url = reverse_lazy('crud:CRUD_list')
    

class CRUDUpdate(UpdateView):
    model = CRUD
    form_class = CRUDForm
    template_name = "crud/crud_update.html"
    success_url = reverse_lazy('crud:CRUD_list')

class CRUDDelete(DeleteView):
    model = CRUD
    success_url = reverse_lazy('crud:CRUD_list')
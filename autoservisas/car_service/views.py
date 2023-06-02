from typing import Any
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . models import Automobilis, AutomobilioModelis, Uzsakymas, UzsakymoEilute, Paslauga





# Create your views here.
from django.http import HttpResponse

def index(request):
    
    num_automobiliai = Automobilis.objects.all().count()
   
    num_automobiliu_modeliai = AutomobilioModelis.objects.all().count()

    num_paslaugos = Paslauga.objects.all().count()

    num_uzsakymas = Uzsakymas.objects.all().count()

    context = {
        'num_automobiliai' : num_automobiliai,
        'num_automobiliu_modeliai' : num_automobiliu_modeliai,
        'num_paslaugos' : num_paslaugos,
        'num_uzsakymai' : num_uzsakymas

    }

    return render(request, 'car_service/index.html', context=context)


def automobiliu_list(request):
    qs = Automobilis.objects.all()
    query = request.GET.get('query')
    if query:
        qs = qs.filter(
            Q(automobilio_modelis__marke__icontains=query)|
            Q( automobilio_modelis__marke__icontains=query)|
            Q(valstybinis_nr__icontains=query)|
            Q(vim_kodas__icontains=query)|
            Q(klientas__icontains=query)
        )
    paginator = Paginator(qs, 5)
    page_number = request.GET.get('page', 1)  # Default to the first page if no page number is provided
    automobiliu_list = paginator.get_page(page_number)
    return render(request, 'car_service/automobiliai.html', {
        'automobiliu_list': automobiliu_list,
    })
    
    
    
    # paginator = Paginator(qs, 5)
    # automobiliu_list = paginator.get_page(request.GET.get('page'))
    # # page = request.GET.get('page', 1)
    # return render(request, 'car_service/automobiliai.html', {
    #     'automobiliu_list': automobiliu_list,
    # })
    # page_number = request.GET.get('page')
    # paged_automobiliai = paginator.get_page(page_number)
    # context = {
    #     'automobiliai': paged_automobiliai
    # }
    
    

def automobiliu_detail(request, pk:int):
    return render(request, 'car_service/automobiliu_detail.html', {
        'automobilis': get_object_or_404(Automobilis, pk=pk)
    })

class UzsakymasView(generic.ListView):
    model = Uzsakymas
    paginate_by = 2
    template_name = 'car_service/uzsakymas_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            qs = qs.filter(
                Q(automobilis__valstybinis_nr__icontains=query) |
                Q(automobilis__vin_kodas__icontains=query) |
                Q(automobilis__klientas__icontains=query)|
                Q(data__icontains=query) 
            )
        return qs

class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymas
    template_name = 'car_service/uzsakymas_detail.html'

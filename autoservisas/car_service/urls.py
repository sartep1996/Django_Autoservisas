from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.index, name='index'),
    path('automobiliai/', views.automobiliu_list, name='automobiliu_list'),
    path('automobilis/<int:pk>/', views.automobiliu_detail, name='automobiliu_detail'),
    path('uzsakymas/', views.UzsakymasView.as_view(), name='uzsakymas_list' ),
    path('uzsakymai/<int:pk>/', views.UzsakymasDetailView.as_view(), name= 'uzsakymas_detail' ),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('mediatheque', views.mediatheque, name='mediatheque'),
    path('bibliotheque', views.bibliotheque, name='bibliotheque'),
    path('contact', views.contact, name='contact'),
    #path('pdf_view/<path:pdf_file_path>/', views.pdf_view, name='pdf_view'),
    path('kedougou', views.destinationTwo, name='destinationTwo'),
    path('blog', views.blog , name='blog'),
    path('details/<str:id>', views.details , name='details'),
]

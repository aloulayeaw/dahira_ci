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
<<<<<<< HEAD
    path('blog_detail', views.blog_detail , name='blog_detail'),
=======
>>>>>>> d0a5e919d2f864f29f246c5777f7be040755b729
    path('details/<str:id>', views.details , name='details'),
]

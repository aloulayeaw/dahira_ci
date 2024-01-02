from django.shortcuts import render
from django.http import HttpResponse
import os
#import fitz

# Create your views here.

def home(request):  

    return render(request, 'base/base.html')

def about(request):
    

    return render(request, 'base/about.html')

def blog(request):
    

    return render(request, 'base/blog.html')

def mediatheque(request):
    

    return render(request, 'base/mediatheque.html')

def bibliotheque(request):
    

    return render(request, 'base/bibliotheque.html')

def contact(request):
    

    return render(request, 'base/contact.html')

# def bibliotheque(request):
#     # Chemin vers le fichier PDF
#     pdf_path = r'D:/data/dahiraci/dahiraci/dahiraci/static/assets/images/fichiers/Optique sur AL MUNTAZAR.pdf'  # Remplacez par le chemin de votre fichier PDF

#     # Ouvrir le fichier PDF avec PyMuPDF
#     pdf_document = fitz.open(pdf_path)

#     # Lire le contenu du PDF en pages
#     pages = []
#     for page_number in range(pdf_document.page_count):
#         page = pdf_document.load_page(page_number)
#         page_text = page.get_text("text")
#         pages.append(page_text)

#     # Fermez le fichier PDF
#     pdf_document.close()

#     context = {
#         'pdf_pages': pages,
#     }

#     return render(request, 'base/bibliotheque.html', context)

# # views.py

# def pdf_view(request, pdf_file_path):
#     # Récupérer le chemin complet du fichier PDF
#     pdf_path = os.path.join(settings.BASE_DIR, pdf_file_path)

#     # Vérifier si le fichier existe
#     if os.path.exists(pdf_path):
#         with open(pdf_path, 'rb') as pdf_file:
#             response = HttpResponse(pdf_file.read(), content_type='application/pdf')
#             response['Content-Disposition'] = f'inline; filename="{os.path.basename(pdf_path)}"'
#             return response
#     else:
#         return HttpResponse("Le fichier PDF n'existe pas", status=404)


def destinationTwo(request):
    

    return render(request, 'base/destinationTwo.html',)


def details(request, id):
    
    # pack= Package.objects.filter(pk=id).values('name_packages','price','description','duree')
    # print(pack)
    
    # context = {
    #     'pack': pack,
    # }

    return render(request, 'base/detailPack.html')
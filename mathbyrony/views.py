from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import os
from django.conf import settings

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


def showpdf(request):
    url = request.GET.get('url',None)
    filepath = os.path.join(settings.BASE_DIR, url[1:])
    with open(filepath, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        # response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed
    
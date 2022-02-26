
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse
from .admin import PostResources
from django.http import HttpResponse



class MainView(TemplateView):
    template_name = 'index.html'


def export(request , format):
    posts_resource = PostResources()
    dataset = posts_resource.export()
    if format == 'csv':
        dataset_Format = dataset.csv
    else:
        dataset_Format = dataset.xls
    
    response = HttpResponse(dataset_Format , content_type=f"text/{format}")
    response['Content-Disposition'] = f"attachment:filename=posts.{format}"
    return response

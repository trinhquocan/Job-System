from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from .models import Category
from rest_framework import viewsets, generics
from .serializer import CategorySerializer

# Create your views here.

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def index(request):
    return HttpResponse('HELLO CS2001')

def list(request, job_id):
    return HttpResponse(f'Job {job_id}')

class CategoryView(View):

    def get(self, request):
        cats = Category.objects.all()
        return render(request, 'anewjob/list.html', {
            'categories': cats
        })

    def post(self, request):
        pass
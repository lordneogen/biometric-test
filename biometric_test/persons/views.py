from rest_framework import generics
from . import serializers
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from . import serializers
from rest_framework.response import Response
from django.core.paginator import Paginator, Page

class list_cr_Persons(APIView):
    
    model=Persons
    queryset =  model.objects.all()
    serializer_class = serializers.SER_CR_Persons
    page_number=1
    
    def get_queryset(self):
        return self.queryset.all()
    
    def get(self, request, *args, **kwargs):
        
        paginator = Paginator(self.queryset, 5)
        
        print(request)
        
        try:
            self.page_number = int(request.GET.get('page'))
    
            if self.page_number==None:
                self.page_number=1
        except:
            self.page_number=1
            
        if paginator.num_pages>=self.page_number and self.page_number>0:
            page = paginator.page(self.page_number)
            serializer = self.serializer_class(data=page, many=True)
            if not serializer.is_valid():
                return Response(serializer.data,status=200)
            else:
               return Response({"error":"Ошибка валидации"},status=500) 
        else:
            return Response({'error':'Нету персон'},status=404)
        
    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data,status=200)
    
class rud_Persons(APIView):
    
    
    model=Persons
    serializer_class = serializers.SER_RUD_Persons
    iin=None
    queryset =None
    
    
    
    def dispatch(self, request, *args, **kwargs):
        self.iin = kwargs.get('id')
        try:
            self.queryset = self.model.objects.get(iin=self.iin)
        except:
            pass
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        
        if self.queryset==None:
            return Response({'error':'Нету персоны'},status=404)
        
        serializer = self.serializer_class(self.queryset)
        return Response(serializer.data,status=200)
        
    def delete(self, request, *args, **kwargs):
        
        if self.queryset==None:
            return Response({'error':'Нету персоны'},status=404)
        self.queryset.delete()
        return Response({"result":"Персона удалена"},status=204)
    
    def put(self, request, *args, **kwargs):
        
        if self.queryset==None:
            return Response({'error':'Нету персоны'},status=404)
        serializer = self.serializer_class(instance=self.queryset, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data,status=200)
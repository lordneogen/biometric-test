from rest_framework import generics
from . import serializers
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from . import serializers
from rest_framework.response import Response

class list_cr_Persons(APIView):
    
    model=Persons
    queryset =  model.objects.all()
    serializer_class = serializers.SER_CR_Persons
    
    
    def get_queryset(self):
        return self.queryset.all()
    
    def get(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=self.get_queryset(), many=True)

        if serializer.is_valid() or len(self.get_queryset())==0 :
            return Response({'error':'Нету персон'},status=404)
        
        return Response(serializer.data)
        
    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data)
    
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
        return Response({"result":"Персона удалена"},status=200)
    
    def put(self, request, *args, **kwargs):
        
        if self.queryset==None:
            return Response({'error':'Нету персоны'},status=404)
        serializer = self.serializer_class(instance=self.queryset, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data,status=200)
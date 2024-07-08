from django.shortcuts import render



# Create your views here.
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.models import *
from app.serializers import *

class ProductCrudViewSet(ViewSet):
    def list(self,request):
        LPO=Product.objects.all()#LPO=list of product object
        JPO=Product_Serializer(LPO,many=True)
        return Response(JPO.data)
    def retrieve(self,request,pk):
        PO=Product.objects.get(pid=pk)
        JO=Product_Serializer(PO)
        return Response(JO.data)
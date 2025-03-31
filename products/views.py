# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from products.serializers import ProductSerializer
from products.models import Product


def productPage(request):
    items = Product.objects.all()
    return render(request, 'products/product.html', {'products': items})


class ProductGetAll(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a list of products",
        responses={
            200: openapi.Response(description="List of products"),
        }
    )
    def get(self, request):
        products = Product.objects.all()
        return Response({'products': ProductSerializer(products ,many=True).data})


class ProductGetById(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a product by its ID",
        responses={
            200: ProductSerializer,
            404: openapi.Response(description="Product not found"),
        }
    )
    
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except:
            return Response({"Error":"Object does not exists"})
        serializer = ProductSerializer(product)
        return Response(serializer.data)
 

class ProductCreate(APIView):
    @swagger_auto_schema(
        operation_description="Create a new product",
        request_body=ProductSerializer,
        responses={
            201: openapi.Response(description="Product created successfully"),
            400: openapi.Response(description="Invalid data"),
        }
    )
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # newProducts = Product.objects.create(
        #     title = request.data['title'],
        #     price = request.data['price'],
        #     description = request.data['description'],
        #     image = request.data['image'],
        #     created_at = request.data['created_at'], 
        # )
        # return Response({'products': ProductSerializer(newProducts).data})
        return Response({'products': serializer.data})
    

class ProductUpdate(APIView):
    @swagger_auto_schema(
        operation_description="Update product",
        responses={
            201: openapi.Response(description="Created successfully"),
            400: openapi.Response(description="Invalid data"),
        }
    )
    
    def put(self,request,*args,**kwargs):
        primary_key = kwargs.get("pk", None)
        if not primary_key:
            return Response({"Error":"Method PUT not alloed"})

        try:
            instance = Product.objects.get(pk=primary_key)
        except:
            return Response({"Error":"Object does not exists"})
        
        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        serializer.save()
        return Response({"product": serializer.data})


class ProductDelete(APIView):
    @swagger_auto_schema(
        operation_description="Delete a product by product Id",
        responses={
            204: openapi.Response(description="Deleted successfully"),
            404: openapi.Response(description="Product not found"),
        }  
    )
    def delete(self,request,id):
        try:
            product = Product.objects.get(id=id)
            print(product)
        except:
            return Response({"Error":"Object does not exists"})
        product.delete()
        return Response(product.data)
 
            
# {
#   "title": "The Flesh",
#   "price": "33",
#   "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
#   "created_at": "2025-03-29",
#   "image":""
# }
# views.py
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from blogs.serializers import BlogSerializer
from blogs.models import Blog


def blogPage(request: HttpRequest):
    items = Blog.objects.all()
    return render(request, 'blogs/blog.html', {'blogs': items})


class BlogGetAll(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a list of blog",
        responses={
            200: openapi.Response(description="List of blogs"),
        }
    )
    def get(self, request):
        blogs = Blog.objects.all()
        return Response({'blogs': BlogSerializer(blogs ,many=True).data})


class BlogGetById(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a blog by its ID",
        responses={
            200: BlogSerializer,
            404: openapi.Response(description="Blog not found"),
        }
    )
    def get(self, request, id):
        try:
            blog = Blog.objects.get(id=id)
        except:
            return Response({"Error":"Object does not exists"})
        serializer = BlogSerializer(blog)
        return Response({'blog': serializer.data})


class BlogCreate(APIView):
    @swagger_auto_schema(
        operation_description="Create a new blog",
        request_body=BlogSerializer,
        responses={
            201: openapi.Response(description="Blog created successfully"),
            400: openapi.Response(description="Invalid data"),
        }
    )
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'blogs': serializer.data})
         


class BlogDelete(APIView):
    @swagger_auto_schema(
        operation_description="Delete a blog by its ID",
        responses={
            204: openapi.Response(description="Blog deleted successfully"),
            404: openapi.Response(description="Blog not found"),
        }
    )
    def delete(self, request, id):
        pass
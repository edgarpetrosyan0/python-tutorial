# serializers.py
from rest_framework import serializers

from products.models import Product


# This is done using a Django ModelSerializer          
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        #fields It is intended to define which fields should be sent to the Frontend.
        fields = ['id',"title","reting","description","imageUrl","created_at"] 
        #If we want to send everything, we use fields = "__all__".

 

# This is done using a manual Django Serializer.
# class ProductSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=25)
#     reting = serializers.DecimalField(max_digits=8, decimal_places=2)
#     description = serializers.CharField(required=True)
#     imageUrl = serializers.URLField(required=True)
#     created_at = serializers.DateField(required=True) 
 
#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data('title', instance.title)
#         instance.reting = validated_data('reting', instance.reting)
#         instance.description = validated_data('description', instance.description)
#         instance.imageUrl = validated_data('imageUrl', instance.imageUrl)
#         instance.created_at = validated_data('created_at', instance.created_at)
#         instance.save()
#         return instance
        

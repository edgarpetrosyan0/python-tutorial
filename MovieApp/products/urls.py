
from django.urls import path
from products.views import * # '*' imports all path views.

# from products.views import (
#     productPage, 
#     ProductGetAll, 
#     ProductGetById, 
#     ProductCreate,
#     ProductUpdate, 
#     ProductDelete
# )

urlpatterns = [
    path('', productListPage, name='product-list'),  # HTML pag
    path('product-detail/<int:id>/', productDetailPage, name='product-detail'), 
    path('product-add/', productAdd, name='product-add'), 
    path("search/", search, name="search"),


    path('api/v3/getAll', ProductGetAll.as_view() ,name=""),  #all products, 
    path('api/v3/<int:id>/', ProductGetById.as_view()),  #product by ID
    path('api/v3/add/', ProductCreate.as_view() ),  #add product
    path('api/v3/update/<int:pk>', ProductUpdate.as_view() ),  #update product
    path('api/v3/delete/<int:id>/', ProductDelete.as_view()),  # delete product
 ]

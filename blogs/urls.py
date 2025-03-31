
from django.urls import path
from blogs.views import * # '*' imports all path views.
# from blogs.views import (
#     blogPage, 
#     BlogGetAll, 
#     BlogGetById, 
#     BlogCreate, 
#     BlogDelete
# )

urlpatterns = [
    path('', blogPage , name='blog'),

    path('api/v3/getAll', BlogGetAll.as_view()),  #all blogs, 
    path('api/v3/<int:id>/',BlogGetById.as_view()), #blog by ID
    path('api/v3/add/',BlogCreate.as_view()),  #add blog
    path('api/v3/delete/<int:id>/',BlogDelete.as_view() ), # delete blog
 ]

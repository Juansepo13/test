from django.urls import path, include
from crud.views import index, create, details, edit, delete

urlpatterns = [
    path('', index, name='index'),
    path('crud/', include('crud.urls')),
    path('create/', create, name='create'),
    path('details/<int:pk>/', details, name='details'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    # ... otras rutas
]



# from django.urls import path, include
# from . import views
# from project.crud.views import index

# urlpatterns = [
#     path('', index, name='index'),
#     path('crud/', include('project.crud.urls')),
#     path('', views.index, name='index'),
#     path('create/', views.create, name='create'),
#     path('details/<int:pk>/', views.details, name='details'),
#     path('edit/<int:pk>/', views.edit, name='edit'),
#     path('delete/<int:pk>/', views.delete, name='delete'),
#     # ... otras rutas
# ]

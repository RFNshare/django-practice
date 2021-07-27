from django.urls import path
from . import views

app_name = 'cats'
urlpatterns = [
    path('', views.cat_list, name='all'),
    path('main/create/', views.cat_create, name='cat_create'),
    path('main/<int:pk>/update/', views.cat_update, name='cat_update'),
    path('main/<int:pk>/delete/', views.cat_delete, name='cat_delete'),
    path('breeds/', views.breeds_list, name='breeds_all'),
    path('breeds/create/', views.breeds_create, name='breed_create'),
    path('breeds/<int:pk>/update/', views.breed_update, name='breed_update'),
    path('breeds/<int:pk>/delete/', views.breed_delete, name='breed_delete'),
    # path('', views.CatList.as_view(), name='all'),
    # path('main/create/', views.CatCreate.as_view(), name='cat_create'),
    # path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
]
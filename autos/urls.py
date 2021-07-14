from django.urls import path
from . import views

app_name = 'autos'
urlpatterns = [
    path('', views.index, name='index'),
    path('crud/', views.autos_crud, name='autos_crud'),
    path('make_create/', views.MakeCreateView.as_view(), name='make_create'),
    path('make_list/', views.MakeListView.as_view(), name='make_list'),
    path('make_update/<str:pk>', views.MakeUpdateView.as_view(), name='make_update'),
    path('make_delete/<str:pk>', views.MakeDeleteView.as_view(), name='make_delete'),
    path('autos_list/', views.AutosListView.as_view(), name='autos_list'),
    path('autos_create/', views.AutosCreateView.as_view(), name='autos_create'),
    path('autos_update/<str:pk>', views.AutosUpdateView.as_view(), name='autos_update'),
    path('autos_delete/<str:pk>', views.AutosDeleteView.as_view(), name='autos_delete'),

]

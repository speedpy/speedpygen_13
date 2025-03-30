from django.urls import path
from .views import crud

urlpatterns = [
    # Part URLs
    path('part/', crud.PartListView.as_view(), name='part_list'),
    path('part/<int:pk>/', crud.PartDetailView.as_view(), name='part_detail'),
    path('part/create/', crud.PartCreateView.as_view(), name='part_create'),
    path('part/<int:pk>/update/', crud.PartUpdateView.as_view(), name='part_update'),
    path('part/<int:pk>/delete/', crud.PartDeleteView.as_view(), name='part_delete'),

    # Container URLs
    path('container/', crud.ContainerListView.as_view(), name='container_list'),
    path('container/<int:pk>/', crud.ContainerDetailView.as_view(), name='container_detail'),
    path('container/create/', crud.ContainerCreateView.as_view(), name='container_create'),
    path('container/<int:pk>/update/', crud.ContainerUpdateView.as_view(), name='container_update'),
    path('container/<int:pk>/delete/', crud.ContainerDeleteView.as_view(), name='container_delete'),

]
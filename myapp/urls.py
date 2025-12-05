from django.urls import path
from .views import DokumenListView, DokumenCreateView, DokumenUpdateView, DokumenDeleteView

urlpatterns = [
    path('', DokumenListView.as_view(), name='dokumen-list'),
    path('upload/', DokumenCreateView.as_view(), name='dokumen-create'),
    path('edit/<int:pk>/', DokumenUpdateView.as_view(), name='dokumen-update'),
    path('delete/<int:pk>/', DokumenDeleteView.as_view(), name='dokumen-delete'),
]
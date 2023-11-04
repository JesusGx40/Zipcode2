from rest_framework import generics
from .models import Registros
from .serializer import ProductoSerializer

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Registros.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registros.objects.all()
    serializer_class = ProductoSerializer
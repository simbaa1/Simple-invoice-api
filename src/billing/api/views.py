from rest_framework import generics
from .serializers import ItemLineSerializer, \
    InvoiceSerializer, UserSerializer, User
from billing.models import Invoice

class InvoiceListCreateView(generics.ListCreateAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()


class ClientListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class InvoiceDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
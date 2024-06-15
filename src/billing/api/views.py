from rest_framework import generics
from .serializers import ItemLineSerializer, \
    InvoiceSerializer, UserSerializer, User
from billing.models import Invoice

class InvoiceCreateView(generics.CreateAPIView):
    serializer_class = InvoiceSerializer


class ClientListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InvoiceDetailView(generics.RetrieveAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
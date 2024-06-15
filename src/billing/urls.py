from django.urls import path
from .api.views import ClientListView, InvoiceDetailView, InvoiceListCreateView


urlpatterns = [
    path("api/clients/", ClientListView.as_view(), name="client-list"),
    path("api/invoice/", InvoiceListCreateView.as_view(), name="invoice-list-create"),
    path("api/invoice/<int:pk>/", InvoiceDetailView.as_view(), name="invoice-detail"),
]

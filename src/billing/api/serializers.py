from rest_framework import serializers
from billing.models import Invoice, ItemLine
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']


class ItemLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLine
        fields=['description', 'price', 'quantity', 'taxed']


class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemLineSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id','invoice_no', 'date', 'due_date', 'status', 'items', 'user']
        extra_kwargs = {"invoice_no": {"required": False, "allow_null": True}}
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)
        for item in items_data:
            ItemLine.objects.create(invoice=invoice, **item)
        return invoice
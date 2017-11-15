from rest_framework.serializers import ModelSerializer
from product.models import Product



class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            ]

class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            ]

class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            ]

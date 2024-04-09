from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

class ProductSerializers(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    tags = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset = Category.objects.all()
    # )
    category = CategorySerializer()
    add_string = serializers.SerializerMethodField(method_name="convert_string") 
    cost = serializers.SerializerMethodField(method_name = "cost_count")

    def cost_count(self, product: Product ):
        return product.price*5

    def convert_string(self, product : Product):

        return f' {product.name} {product.tags} '



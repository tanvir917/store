from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'featured_product']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['featured_product'] = instance.featured_product.title if instance.featured_product else None
        return representation

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'inventory','unit_price', 'price_with_tax', 'collection']
        #fields = '__all__'  # Use this to include all fields from the model
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # description = serializers.CharField()
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_price_with_tax')
    # inventory = serializers.IntegerField()
    # last_update = serializers.DateTimeField()

    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection_detail'
    # )
    #collection = CollectionSerializer()
    #collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
    #collection = serializers.StringRelatedField()
    # promotion = serializers.ListField(
    #     child=serializers.CharField(source='description'),
    #     allow_empty=True
    # )

    def calculate_price_with_tax(self, product: Product):
        return product.unit_price * Decimal(1.15)
    
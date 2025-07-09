from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    inventory = serializers.IntegerField()
    last_update = serializers.DateTimeField()
    # collection = serializers.CharField(source='collection.title')
    # promotion = serializers.ListField(
    #     child=serializers.CharField(source='description'),
    #     allow_empty=True
    # )
from rest_framework import serializers
from .models import Image, ShopItems
from django.db.models import fields

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image',]

class ShopItemSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, read_only=False)

    def create(self, validated_data):
        images_data = validated_data.pop("image")
        shop_item = ShopItems.objects.create(**validated_data)
        for image_data in images_data:
            Image.objects.create(shop_item=shop_item, image=image_data['image'])
        return shop_item
    
    class Meta:
        model = ShopItems
        fields = [
            'id',
            'item_name',
            'item_price',
            'item_author',
            'date',
            'image',
        ]


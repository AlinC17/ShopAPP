from django.shortcuts import render
from django.http import HttpResponse, Http404

from .serializers import ShopItemSerializer
from .forms import CreateShopItemForm, ImageForm
from .models import ShopItems, Image

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here. 
def index(request):
    imageform = ImageForm()
    form = CreateShopItemForm()

    return render(request, 'main/index.html', {"form": form, "imageform": imageform})

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/all',
        'Add': '/create',
        'Update': '/update/id/',
        'Delete': '/item/delete/id/'
    }
  
    return Response(api_urls)

@api_view(['GET'])
def get_all_item_data(request):
    try:
        shop_items = ShopItems.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if shop_items:
        data = ShopItemSerializer(shop_items, many=True)
        print(data.field_name)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_item_data(request, id):
    try:
        shop_item = ShopItems.objects.get(pk=id)
        data = ShopItemSerializer(shop_item)
        return Response(data.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_item(request):
    data = request.data
    images = []
    for image in data.getlist('image'):
        images.append({'image': image})
    data = data.dict()
    data['image']= images
    shop_item = ShopItemSerializer(data=data)
    print(data)
    if shop_item.is_valid():
        shop_item.save()
        print('success')
        return Response(shop_item.data)
    else:
        print("invalid")
        print(shop_item.errors)
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_item(request, id):
    try:
        shop_item = ShopItems.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if shop_item:
        shop_item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def update_item(request, id):
    try:
        shop_item = ShopItems.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = request.data
    images = []
    for image in data.getlist('image'):
        images.append({'image': image})
    data = data.dict()
    data['image'] = images
    final_data = ShopItemSerializer(instance=shop_item, data=request.data)
  
    if final_data.is_valid():
        final_data.save()
        return Response(final_data.data)
    else:
        return Response(status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)


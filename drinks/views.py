from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        seriallizer = DrinkSerializer(drinks, many=True)
        return Response(seriallizer.data)
    if request.method == 'POST':
        seriallizer = DrinkSerializer(data=request.data)
        if seriallizer.is_valid():
            seriallizer.save()
            return Response(seriallizer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, fromat=None):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors(status.HTTP_400_BAD_REQUEST))
    
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
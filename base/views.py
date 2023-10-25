from .models import Product
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

@api_view(['GET', 'POST', 'DELETE', 'PUT'])  # Include 'PUT' for update
def products(request, product_id=None):
    if request.method == 'GET':
        products = Product.objects.all()
        product_list = []

        for product in products:
            product_dict = {
                "id": product.id,
                "description": product.description,
                "price": str(product.price),
                "category": product.category
            }
            product_list.append(product_dict)

        return Response(product_list, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        description = data.get('description')
        price = data.get('price')
        category = data.get('category')

        if not (description and price and category):
            return Response({'error': 'Incomplete data'}, status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.create(
            description=description,
            price=price,
            category=category
        )

        return Response({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        if product_id is not None:
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
            
            data = request.data
            description = data.get('description')
            price = data.get('price')
            category = data.get('category')

            if description is not None:
                product.description = description
            if price is not None:
                product.price = price
            if category is not None:
                product.category = category
            
            product.save()
            
            return Response({'message': 'Product updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Product ID is required for updating'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            raise Http404

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Item
from .serializers import ItemSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.core.cache import cache

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]


# class Items(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         serializer = ItemSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'Message': 'Item Added Successfully.'})

#     @method_decorator(cache_page(60 * 60 * 2))
#     @method_decorator(vary_on_headers("Authorization"))
#     def get(self, request, format=None):
#         items = Item.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return Response(serializer.data)


# class GetUpdateItem(APIView):

#     permission_classes = [IsAuthenticated]

#     def get_object(self, pk):
#         try:
#             return Item.objects.get(pk=pk)
#         except Item.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         if pk<=0:
#             return Response({"Message": "Negative OR Zero Indexing is Not Supported"})
#         else:    
#             items = Item.objects.filter(id = pk)
#             serializer = ItemSerializer(items, many=True)
#             return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         item = self.get_object(pk)
#         serializer = ItemSerializer(item, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'Message': 'Item Updated Successfully'})



import logging
logger = logging.getLogger(__name__)

def create(self, request, *args, **kwargs):
    logger.info(f"Creating item with data: {request.data}")
    return super().create(request, *args, **kwargs)


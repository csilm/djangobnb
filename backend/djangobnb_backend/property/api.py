from django.http import JsonResponse #type: ignore

from rest_framework.decorators import api_view, authentication_classes, permission_classes #type: ignore

from .models import Property
from .serializers import PropertiesListSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_list(request):
    properties = Property.objects.all()
    serializer = PropertiesListSerializer(properties, many = True)
    return JsonResponse({
        'data': serializer.data
    })
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.models import User


# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def UserView(request):
#    serializer = UserSerializer(request.user)
#    return Response(serializer.data)  # Devuelve en formato JSon


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

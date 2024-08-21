from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.views.decorators.csrf import csrf_exempt


@api_view(['POST'])
@csrf_exempt
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.user.is_authenticated:
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            return Response({'error': 'Token not found or user not authenticated.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'Logged out successfully.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'User is not authenticated.'}, status=status.HTTP_400_BAD_REQUEST)
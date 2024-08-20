from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from forum.models import Forum
from forum.serializers import ForumSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def forum_create(request):
    serializer = ForumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'forum': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def forum_list(request):
    try:
        forums = Forum.objects.all()
        serializer = ForumSerializer(forums, many=True)
        return Response({'forums': serializer.data})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def forum_detail(request, pk):
    try:
        forum = Forum.objects.get(pk=pk)
        serializer = ForumSerializer(forum)
        return Response({'forum': serializer.data})
    except Forum.DoesNotExist:
        return Response({'error': 'Forum not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def forum_update(request, pk):
    try:
        forum = Forum.objects.get(pk=pk)
    except Forum.DoesNotExist:
        return Response({'error': 'Forum not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ForumSerializer(forum, data=request.data, partial=True)  # partial=True para atualizações parciais
    if serializer.is_valid():
        serializer.save()
        return Response({'forum': serializer.data})
    return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def forum_delete(request, pk):
    try:
        forum = Forum.objects.get(pk=pk)
    except Forum.DoesNotExist:
        return Response({'error': 'Forum not found'}, status=status.HTTP_404_NOT_FOUND)

    forum.delete()
    return Response({'message': 'Forum deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
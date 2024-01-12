from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Posts
from .serializer import PostsSerializer


class PostView(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


@api_view(['GET'])
def posts_list(request):
    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def posts_get(request, pk):
    post = Posts.objects.get(pk=pk)
    serializer = PostsSerializer(post)
    return Response(serializer.data)


@api_view(['DELETE'])
def post_del(request, pk):
    post = Posts.objects.get(pk=pk)
    post.delete()
    return Response('Post deleted')


@api_view(['CREATE'])
def post_add(request):
    serializer = PostsSerializer(data=request.data)
    if serializer.is_valid():
        post = serializer.save()
        return Response('Post added')


@api_view(['POST'])
def post_put(request, pk):
    post = Posts.objects.get(pk=pk)
    serializer = PostsSerializer(data=request.data, instance=post)
    if serializer.is_valid():
        post = serializer.save()
    return Response(serializer.data)


@api_view(['PATCH'])
def post_update(request, pk):
    post = Posts.objects.get(pk=pk)
    serializer = PostsSerializer(data=request.data, instance=post, partial=True)
    if serializer.is_valid():
        post = serializer.save()
    return Response(serializer.data)

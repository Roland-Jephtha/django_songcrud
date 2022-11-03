from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from .models import Song
from rest_framework.response import Response
from .serializers import SongSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def getSongs(request):
    song = Song.objects.all()
    serializer = SongSerializer(song, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def getSong(request, pk):
    song = Song.objects.get(id = pk)
    serializer = SongSerializer(song, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def addSong(request):
    data = request.data
    song = Song.objects.create(
        title = data['title'],
        detail = data['detail']
    )
    serializer = SongSerializer(song, many = False)
    return Response(serializer.data)


@api_view(['PUT'])
def updatesong(request, pk):
    data = request.data
    song = Song.objects.get(id = pk)
    serializer = SongSerializer(song, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(["DELETE"])
def deleteSong(request, pk):
    song = Song.objects.get(id = pk).delete()
    return Response("Note was Deleted")
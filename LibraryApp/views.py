from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from django.shortcuts import render
from .serializers import BookSerializer, TrackerSerializer, NoteSerializer
from .models import Book, Tracker, Note, User

@api_view(['GET'])
def home(request, format=None):
    return Response({
        'books': reverse('book_list', request=request, format=format),
        'tracks': reverse('track_list', request=request, format=format),
        'notes': reverse('notes_list', request=request, format=format),
    })

# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    
    def get(self, request, pk, format=None):
        """
        Return a list of all books.
        """
        books = Book.objects.filter(id=pk)
        serializer = BookSerializer(books, many=True,context={'request': request})
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        """
        Allow admin to update a book.
        """
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self,request, pk, format=None):
        permission_classes = (permissions.IsAdminUser,)
        """
        Note that only admins should be able to perform this action
        """
        book = Book.objects.get(id=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TrackerList(generics.ListCreateAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TrackerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        """
        Return a list of all tracks.
        Note That only the user tracking should be able to see
        """
        tracked = Tracker.objects.filter(user=request.user)
        serializer = TrackerSerializer(tracked, many=True,context={'request': request})
        return Response(serializer.data)

    def post(self,request,format=None):
        """
        Allow user to tack a book.
        Note that only the user should be able to perform action
        """
        serializer = TrackerSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NotesList(generics.ListCreateAPIView):
    queryset = Note.objects.all
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all
    serializer_class = TrackerSerializer
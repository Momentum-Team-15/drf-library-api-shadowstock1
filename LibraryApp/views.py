from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book

@api_view(['GET'])
def home(request, format=None):
    return Response({
        'books': reverse('book_list', request=request, format=format),
    })
# Create your views here.
class BookList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        """
        Return a list of all books.
        """
        # query for all the books
        books = Book.objects.all()
        # serialize the data so that I can return habits as json
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Add a new book.
        Need the pk of an existing user for this.
        The IsAuthenticatedOrReadOnly permission class (set in settings) will
        ensure that I have a logged in user.
        """
        # the body of the request has the info to create a new habit
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
        # if that all checks out, we still need to associate the user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
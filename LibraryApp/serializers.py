from rest_framework import serializers
from LibraryApp.models import Book, Tracker, Note, User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date','featured']

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = ['url', 'id', 'book', 'user','status']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['user', 'book', 'notes', 'created_at', 'private']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username') 

from rest_framework import serializers
from .models import Genre, Book, Author

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'first_name',
            'last_name',
        ]


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'summary',
            'isbn',
            'genre',
        ]

class BookListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'summary',
            'isbn',
            'genre',
        ]
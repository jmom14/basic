# pylint: disable=E1101:no-member
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .models import Book
from rest_framework import mixins


class RankingViewDetail(APIView, mixins.CreateModelMixin):

    get_serializer = serializers.RatingSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookList(APIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    get_serializer = serializers.BookSerializer

    def paginate_queryset(self, queryset=None):
        return None

    def filter_queryset(self, queryset):
        return queryset

    def get_queryset(self):
        return Book.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookDetail(APIView, mixins.CreateModelMixin, mixins.RetrieveModelMixin):

    def get_object(self):
        return Book.objects.get(pk=self.kwargs["pk"])

    def get_serializer(self, instance=None):
        return serializers.BookSerializer(instance)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# localhost: 8000/api/v1/books/1/rating
@api_view(["GET"])
def book_detail(request, pk):
    print(pk)
    return Response({"message": "Hello, world!"})


# localhost:8000/api/v1/books/1/rating
@api_view(["POST"])
def rate_book(request, pk):
    print(pk)
    return Response({"message": "Hello, world!"})

from .models import Book, Rating
from rest_framework import serializers
from django.db.models import Avg, Max, Min, Count


class BookSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    max_rating = serializers.SerializerMethodField()
    min_rating = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()

    def get_rating(self, book):
        return book.rating_set.aggregate(Avg("score", default=0))["score__avg"]

    def get_max_rating(self, book):
        return book.rating_set.aggregate(Max("score", default=0))["score__max"]

    def get_min_rating(self, book):
        return book.rating_set.aggregate(Min("score", default=0))["score__min"]

    def get_count_rating(self, book):
        return book.rating_set.aggregate(Count("score"))["score__count"]

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "rating",
            "max_rating",
            "min_rating",
            "count_rating",
        ]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

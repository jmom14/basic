from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(
    "",
    views.RankingViewDetail,
    basename="ranking",
)


urlpatterns = [
    path(r"<int:pk>/ranking", views.RankingViewDetail.as_view()),
    path(r"<int:pk>", views.BookDetail.as_view()),
    path("", views.BookList.as_view()),
]

from django.urls import path

from ebooks.views import EbookListCreateAPIView, EbookDetailAPIView, ReviewListCreateAPIView, ReviewDetailAPIView

urlpatterns = [
    path('ebooks/', EbookListCreateAPIView.as_view(), name="ebook-list"),
    path('ebooks/<int:pk>/', EbookDetailAPIView.as_view(), name="ebook-detail"),
    path('ebooks/<int:ebook_pk>/review/', ReviewListCreateAPIView.as_view(), name="review-list"),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name="review-detail"),
]

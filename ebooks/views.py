from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework import mixins

from ebooks.models import Ebook, Review
from ebooks.serializers import EbookSerializer, ReviewSerializer
from ebooks.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from ebooks.paginations import SmallSetPagination


class EbookListCreateAPIView(ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("id")
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination


class EbookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        review_author = self.request.user
        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)
        if review_queryset.exists():
            raise ValidationError("Siz avval sharx qoldirgansiz!")
        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

# class EbookListCreateAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

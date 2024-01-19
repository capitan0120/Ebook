from rest_framework import pagination


class SmallSetPagination(pagination.PageNumberPagination):
    page_size = 3

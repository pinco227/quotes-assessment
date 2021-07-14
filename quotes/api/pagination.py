from rest_framework.pagination import PageNumberPagination


class QuotesPagination(PageNumberPagination):
    page_size = 30
